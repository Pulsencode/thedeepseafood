from datetime import datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, send_mail
from django.core.validators import validate_email
from django.http import HttpResponseRedirect, JsonResponse
from django.template import loader
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from company.models import (
    # AboutUs,
    BlogDetails,
    Brand,
    Certification,
    CompanyTestimonial,
    ContactUsDetails,
    EnquiryDetails,
    EventGallery,
    HistoryDetails,
    ManagementTeam,
    NewsDetails,
    SEO,
    Supermarkets,
    PromotionDetails,
)
from career.models import VaccancyDetails, ApplicationDetails
from products.models import Category, Product, ProductDetails, RecipeDetails


class MeetingView(TemplateView):
    template_name = "meeting.html"


class CatalogueView(TemplateView):
    template_name = "catalogue.html"


class IndexView(TemplateView):
    template_name = "website/index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = (
            Brand.objects.filter(status=True)
            .exclude(name="Deep Sea")
            .order_by("sequence")
        )
        category = Category.objects.filter(status=True).order_by("-id")
        product = Product.objects.filter(
            brand__name="Deep Sea", status=True, homepage=True
        ).order_by("sequence")[:9]
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        testimonial = CompanyTestimonial.objects.filter(status=True).order_by("-id")
        type = ""
        certification = Certification.objects.filter(status=True).order_by("-id")
        # Log product information
        # logger.info(f"Product information: {product}")
        # context["data"] = SEO.objects.filter(page="Home").first()
        context["certification"] = certification
        context["testimonial"] = testimonial
        context["type"] = type
        context["blog"] = blog
        context["product"] = product
        context["category"] = category
        context["brands"] = brand
        return context


class IndexProductView(View):
    template_name = "website/index/product_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            type = request.GET.get("ptype")
            print(type, "**")
            try:
                if type == "All":
                    product = Product.objects.filter(
                        status=True, brand__name="Deep Sea", homepage=True
                    ).order_by("sequence")[:9]
                    context = {"product": product}
                else:
                    product = Product.objects.filter(
                        status=True, brand__name="Deep Sea", type=type, homepage=True
                    ).order_by("sequence")[:9]

                    context = {"product": product, "type": type}

                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse({"status": True, "template": html_content})
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class AboutView(TemplateView):
    template_name = "website/about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = ManagementTeam.objects.filter(status=True).order_by("sequence")
        history = HistoryDetails.objects.filter(status=True).order_by("id")
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # about1 = AboutUs.objects.filter(status=True).order_by("-id")[:1]
        # about2 = AboutUs.objects.filter(status=True).order_by("-id")[1:2]
        # about3 = AboutUs.objects.filter(status=True).order_by("-id")[2:3]
        # about4 = AboutUs.objects.filter(status=True).order_by("-id")[3:4]
        # context["data"] = SEO.objects.filter(page="About").first()
        # context["about1"] = about1
        # context["about2"] = about2
        # context["about3"] = about3
        # context["about4"] = about4
        context["blog"] = blog
        context["history"] = history
        context["teams"] = teams
        return context


class ProductView(TemplateView):
    template_name = "website/products/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = self.request.GET.get("type")
        if type:
            product = Product.objects.filter(
                brand__name="Deep Sea", type=type, status=True
            ).order_by("sequence")
        else:
            product = Product.objects.filter(
                brand__name="Deep Sea", status=True
            ).order_by("sequence")
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Product").first()
        context["blog"] = blog
        context["type"] = type
        context["product"] = product
        return context


class ProductListingView(View):
    template_name = "website/products/product_lists.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            type = request.GET.get("ptype")
            print(type, "**")
            try:
                if type == "All":
                    product = Product.objects.filter(
                        status=True, brand__name="Deep Sea"
                    ).order_by("sequence")
                else:
                    product = Product.objects.filter(
                        status=True, brand__name="Deep Sea", type=type
                    ).order_by("sequence")

                context = {
                    "product": product,
                }

                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse({"status": True, "template": html_content})
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class ProductDetailsView(TemplateView):
    template_name = "website/products/product-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug_product = self.kwargs["slug_product"]
        product = Product.objects.get(slug_product=slug_product)
        cat = (
            product.product_details.filter(status=True)
            .order_by("category__sequence")
            .values_list("category__id", flat=True)
            .distinct()
            .first()
        )
        cat_name = (
            product.product_details.filter(status=True)
            .order_by("category__sequence")
            .values_list("category__name", flat=True)
            .distinct()
            .first()
        )
        # cat = Category.objects.filter(status=True,brand__name='Deep Sea').order_by('-id').first()
        # data = ProductDetails.objects.filter(product=product,category=cat)
        # print(data.price)
        try:
            data = ProductDetails.objects.filter(product=product, category=cat).first()
        except ProductDetails.DoesNotExist:
            data = None
        list = (
            Product.objects.filter(status=True, brand__name="Deep Sea")
            .exclude(slug_product=slug_product)
            .order_by("sequence")[:6]
        )
        category = Category.objects.filter(
            status=True, brand__name="Deep Sea"
        ).order_by("sequence")
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        context["blog"] = blog
        context["category"] = category
        context["cat_name"] = cat_name
        context["cat"] = cat
        context["list"] = list
        context["data"] = data
        context["product"] = product
        return context


class GeneralProductDetailsView(View):
    template_name = "website/products/details.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            cid = request.GET.get("cid")
            pid = request.GET.get("pid")

            try:
                # category = Category.objects.filter(brand__name='Oceano',status=True).order_by('-id')
                cat = Category.objects.get(id=cid)
                products = Product.objects.get(id=pid)
                # data = ProductDetails.objects.get(product=products,category=cat)
                try:
                    data = ProductDetails.objects.get(product=products, category=cat)
                except ProductDetails.DoesNotExist:
                    data = None
                context = {
                    "cat_name": cat,
                    "data": data,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {
                        "status": True,
                        "template": html_content,
                    }
                )
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class SearchProductView(View):
    template_name = "website/products/search_product.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            input = request.GET.get("input")
            type = request.GET.get("type")
            # print(type,'***type')

            try:
                if type != "" and type != "All":
                    product = Product.objects.filter(
                        status=True,
                        brand__name="Deep Sea",
                        type=type,
                        name__icontains=input,
                    ).order_by("sequence")

                # print(product)
                else:
                    product = Product.objects.filter(
                        status=True, brand__name="Deep Sea", name__icontains=input
                    ).order_by("sequence")

                # Get distinct categories related to the retrieved products
                categories = Category.objects.filter(
                    product_category__product__in=product
                ).distinct()
                context = {"product": product, "categories": categories}
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {
                        "status": True,
                        "template": html_content,
                    }
                )
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class BrandView(TemplateView):
    template_name = "website/brands/brands.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supermarkets = Supermarkets.objects.filter(status=True).order_by("-id")
        recipes = RecipeDetails.objects.filter(status=True).order_by("-id")
        category = Category.objects.filter(brand__name="Oceano", status=True).order_by(
            "sequence"
        )
        first_category = category.first()
        products = Product.objects.filter(
            status=True, brand__name="Oceano", product_details__category=first_category
        ).order_by("sequence")[:4]
        total_product = (
            Product.objects.filter(
                status=True,
                brand__name="Oceano",
                product_details__category=first_category,
            )
            .order_by("-id")
            .count()
        )
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Oceano").first()
        context["blog"] = blog
        # print(total_product,'***')
        context["category"] = category
        context["total_product"] = total_product
        context["products"] = products
        context["recipes"] = recipes
        context["supermarkets"] = supermarkets
        return context


class ProductContentView(View):
    template_name = "website/brands/products_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            type = request.GET.get("type")
            print(type, "**")
            try:

                products = Product.objects.filter(
                    status=True,
                    brand__name="Oceano",
                    product_details__category__name=type,
                ).order_by("sequence")[:4]
                total_count = (
                    Product.objects.filter(
                        status=True,
                        brand__name="Oceano",
                        product_details__category__name=type,
                    )
                    .order_by("-id")
                    .count()
                )

                context = {
                    "total_count": total_count,
                    "products": products,
                }

                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {
                        "status": True,
                        "template": html_content,
                        "total_count": total_count,
                    }
                )
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


def load_more_product(request):
    try:
        offset = int(request.GET["offset"])
        limit = int(request.GET["limit"])
        type = request.GET["type"]

        total_count = (
            Product.objects.filter(
                status=True, brand__name="Oceano", product_details__category__name=type
            )
            .order_by("-id")
            .count()
        )
        # print(total_count,'***')
        data = Product.objects.filter(
            status=True, brand__name="Oceano", product_details__category__name=type
        ).order_by("sequence")[offset : offset + limit]

        t = render_to_string(
            "website/brands/product_load.html",
            {"data": data, "total_count": total_count},
        )
        return JsonResponse({"data": t, "status": True, "total_count": total_count})
    except Product.DoesNotExist:
        return JsonResponse({"error": "type not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


class OceanoProductDetailsView(View):
    template_name = "website/brands/product_details.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            id = request.GET.get("id")
            print(id, "**")
            try:
                category = Category.objects.filter(
                    brand__name="Oceano", status=True
                ).order_by("sequence")
                # cat = Category.objects.filter(brand__name='Oceano',status=True).order_by('-id').first()

                products = Product.objects.get(id=id)
                print(products)
                cat = (
                    products.product_details.filter(status=True)
                    .values_list("category__id", flat=True)
                    .order_by("-id")
                    .distinct()
                    .first()
                )
                print(cat)
                try:
                    data = ProductDetails.objects.get(product=products, category=cat)
                except ProductDetails.DoesNotExist:
                    data = None

                context = {
                    "products": products,
                    "category": category,
                    "data": data,
                    "cat": cat,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {
                        "status": True,
                        "template": html_content,
                    }
                )
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class OceanoModalProductDetailsView(View):
    template_name = "website/brands/product_data.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            cid = request.GET.get("cid")
            id = request.GET.get("id")

            try:
                category = Category.objects.filter(
                    brand__name="Oceano", status=True
                ).order_by("sequence")
                cat = Category.objects.get(id=cid)
                products = Product.objects.get(id=id)
                try:
                    data = ProductDetails.objects.get(product=products, category=cat)
                except ProductDetails.DoesNotExist:
                    data = None
                context = {
                    "products": products,
                    "category": category,
                    "data": data,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {
                        "status": True,
                        "template": html_content,
                    }
                )
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)


class BrandsListView(TemplateView):
    template_name = "website/brands/brands_list.html"


class DistributionView(TemplateView):
    template_name = "website/distribution/distribution.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["data"] = SEO.objects.filter(page="Distribution Channel").first()
        return context


class NewsRoomView(TemplateView):
    template_name = "website/news/news-room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = EventGallery.objects.filter(status=True).order_by("sequence")
        total_events = EventGallery.objects.filter(status=True).count()

        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="News Room").first()
        context["blog"] = blog
        context["gallery"] = gallery
        context["total_events"] = total_events
        return context


class LoadEvents(View):
    template_name = "website/news/event_gallery.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":

            try:
                gallery = EventGallery.objects.filter(status=True).order_by("sequence")[
                    :3
                ]
                total_events = EventGallery.objects.filter(status=True).count()
                context = {
                    "gallery": gallery,
                    "total_events": total_events,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse({"status": True, "template": html_content})
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


class LoadNews(View):
    template_name = "website/news/news_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":

            try:
                news = NewsDetails.objects.filter(
                    status=True, type="Company News"
                ).order_by("sequence")[:3]
                total_news = NewsDetails.objects.filter(
                    status=True, type="Company News"
                ).count()
                context = {
                    "news": news,
                    "type": "Company News",
                    "total_news": total_news,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {"status": True, "template": html_content, "total_news": total_news}
                )
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


class LoadGlobalNews(View):
    template_name = "website/news/news_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":

            try:
                news = NewsDetails.objects.filter(
                    status=True, type="Global News"
                ).order_by("sequence")[:3]
                total_news = NewsDetails.objects.filter(
                    status=True, type="Global News"
                ).count()
                context = {
                    "news": news,
                    "type": "Global News",
                    "total_news": total_news,
                }
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse(
                    {"status": True, "template": html_content, "total_news": total_news}
                )
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


class LoadPromotions(View):
    template_name = "website/news/promotions_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":

            try:
                promotion = PromotionDetails.objects.filter(status=True).order_by("-id")

                context = {"promotion": promotion}
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse({"status": True, "template": html_content})
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


def load_more_news(request):
    offset = int(request.GET["offset"])
    limit = int(request.GET["limit"])
    type = request.GET["type"]
    data = NewsDetails.objects.filter(status=True, type=type).order_by("sequence")[
        offset : offset + limit
    ]
    total_news = NewsDetails.objects.filter(status=True, type=type).count()
    t = render_to_string(
        "website/news/loadmore_news.html",
        {"data": data, "type": type, "total_news": total_news},
    )
    return JsonResponse({"data": t})


def load_more_events(request):
    offset = int(request.GET["offset"])
    limit = int(request.GET["limit"])
    # type = request.GET['type']
    data = EventGallery.objects.filter(status=True).order_by("sequence")[
        offset : offset + limit
    ]
    total_events = EventGallery.objects.filter(status=True).count()
    t = render_to_string(
        "website/news/loadmore_events.html",
        {"data": data, "total_events": total_events},
    )
    return JsonResponse({"data": t})


class NewsDetailsView(TemplateView):
    template_name = "website/news/news-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        data = NewsDetails.objects.get(pk=id)
        news = NewsDetails.objects.filter(status=True).exclude(id=id).order_by("-id")
        # blog = BlogDetails.objects.filter(status=True).order_by('-id')
        # context['blog'] = blog
        context["data"] = data
        context["news"] = news
        return context


class NewsListsView(TemplateView):
    template_name = "website/news/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = NewsDetails.objects.filter(status=True).order_by("-id")
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        context["blog"] = blog
        context["news"] = news
        return context


class PromotionView(TemplateView):
    template_name = "website/promotion/promotion-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        promotion = PromotionDetails.objects.get(pk=id)
        data = (
            PromotionDetails.objects.filter(status=True).exclude(id=id).order_by("-id")
        )
        context["data"] = data
        context["promotion"] = promotion
        return context


class CareerView(TemplateView):
    template_name = "website/career/career.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        careers = VaccancyDetails.objects.filter(status=True).order_by("-id")
        types_list = [career.type.split(", ") for career in careers]
        print(types_list)
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Career").first()
        context["blog"] = blog
        context["types_list"] = types_list
        context["careers"] = careers
        return context


class BlogView(TemplateView):
    template_name = "website/blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Blogs").first()
        context["blog"] = blog
        return context


class BlogDetailsView(TemplateView):
    template_name = "website/blog/blog-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        data = BlogDetails.objects.get(slug=slug)
        blog = (
            BlogDetails.objects.filter(status=True).exclude(slug=slug).order_by("-id")
        )
        # list = BlogDetails.objects.filter(status=True).order_by('-id')
        # context['blog'] = list
        context["data"] = data
        context["blogs"] = blog
        return context


class ContactView(TemplateView):
    template_name = "website/contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch = self.request.GET.get("branch")
        blog = BlogDetails.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Contact Us").first()
        context["blog"] = blog
        context["branch"] = branch
        return context


class SendEmailView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        location = request.POST["location"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message = request.POST["message"]
        honey = request.POST["honey"]
        # Validate email
        try:
            validate_email(email)
        except ValidationError as e:
            print(e)
            messages.error(request, "Invalid email..Please try again..!!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if honey:
            # Honey field is not empty, indicating potential spam
            messages.error(request, "Error: Form submission not allowed.")
        else:
            # Honey field is empty, proceed with sending the email
            if name and location and phone and email:
                contact = ContactUsDetails(
                    name=name,
                    email=email,
                    location=location,
                    mobile_no=phone,
                    message=message,
                )
                contact.save()
                subject = "New Form Submission-Deep Seafood Company Website"
                message_body = f"Name: {name}\nLocation: {location}\nMobile: {phone}\nEmail: {email}\nMessage: {message}"
                from_email = "deepseafood.connect@gmail.com"
                to_email = "info@thedeepseafood.com"
                send_mail(subject, message_body, from_email, [to_email])

                messages.info(request, "Your Request Shared Successfully")
            else:
                messages.warning(request, "Please Fill All Fields Correctly!")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ProductEnquiryView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        location = request.POST["location"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        product = request.POST["product"]
        message = request.POST["message"]
        honey = request.POST["honey"]
        # Validate email
        try:
            validate_email(email)
        except ValidationError as e:
            print(e)
            messages.error(request, "Invalid email..Please try again..!!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if honey:
            # Honey field is not empty, indicating potential spam
            messages.error(request, "Error: Form submission not allowed.")
        else:
            # Honey field is empty, proceed with sending the email
            if name and location and phone and email:
                enquiry = EnquiryDetails(
                    product=product,
                    name=name,
                    email=email,
                    location=location,
                    mobile_no=phone,
                    message=message,
                )
                enquiry.save()
                subject = "New Form Submission-Deep Seafood Company Website"
                message_body = f"Enquiry for: {product}\nName: {name}\nLocation: {location}\nMobile: {phone}\nEmail: {email}\nMessage: {message}"
                from_email = "deepseafood.connect@gmail.com"
                to_email = "info@thedeepseafood.com"
                send_mail(subject, message_body, from_email, [to_email])

                messages.info(request, "Your Request Shared Successfully")
            else:
                messages.warning(request, "Please Fill All Fields Correctly!")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class CareerEmailView(View):
    def post(self, request, *args, **kwargs):
        applied = request.POST["applied"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        period = request.POST["notice_period"]
        attachment = request.FILES["attachment"]
        cover = request.FILES.get("cover", None)
        linkedin = request.POST["linkedin"]
        message = request.POST["message"]
        honey = request.POST["honey"]
        portfolio = request.POST["portfolio"]
        date_str = request.POST.get("date")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            date = None
        # Validate email
        try:
            validate_email(email)
        except ValidationError as e:
            print(e)
            messages.error(request, "Invalid email..Please try again..!!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if honey:
            # Honey field is not empty, indicating potential spam
            messages.error(request, "Error: Form submission not allowed.")
        else:
            # Honey field is empty, proceed with sending the email
            if period and first_name and phone and email:
                application_details = ApplicationDetails(
                    job=applied,
                    first_name=first_name,
                    last_name=last_name,
                    date=date,
                    portfolio=portfolio,
                    email=email,
                    mobile_no=phone,
                    notice=period,
                    linkedin=linkedin,
                    message=message,
                    attachment=attachment if attachment else None,
                    cover=cover if cover else None,
                )
                application_details.save()

                subject = "New Form Submission-Deep Seafood Company Website"
                message_body = f"First Name: {first_name}\nLast Name: {last_name}\nDate Of Birth: {date}\nMobile: {phone}\nEmail: {email}\nNotice Period:{period}\nPortfolio: {portfolio}\nLinkedIn:{linkedin}\nMessage: {message}"
                email_message = EmailMessage(
                    subject,
                    message_body,
                    "deepseafood.connect@gmail.com",
                    ["info@thedeepseafood.com"],
                )

                # Attach the file if provided
                if attachment:
                    email_message.attach(
                        attachment.name, attachment.read(), attachment.content_type
                    )

                # Attach the cover letter if provided
                if cover:
                    email_message.attach(cover.name, cover.read(), cover.content_type)

                # Send the email
                email_message.send()

                messages.info(request, "Your Request Shared Successfully")
            else:
                messages.warning(request, "Please Fill All Fields Correctly!")

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
