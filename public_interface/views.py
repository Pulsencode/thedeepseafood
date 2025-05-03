from django.shortcuts import render, get_object_or_404
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
    Blog,
    Brand,
    Certification,
    CompanyTestimonial,
    ContactUs,
    Enquiry,
    Event,
    History,
    ManagementTeam,
    News,
    # SEO,
    Supermarkets,
    Promotion,
)
from career.models import VacancyDetails
from products.models import Category, Product, ProductDetails
from career.forms import ApplicationDetailsForm


def home(request):
    all_products = Product.objects.all().order_by("sequence")
    homepage_products = Product.objects.filter(homepage=True).order_by("sequence")[:9]

    # If no homepage marked, show the first 9 of all products
    if not homepage_products:
        display_products = all_products[:9]
    else:
        display_products = homepage_products

    context = {
        "page_title": "Wholesale Seafood Export & Import Supplier in UAE, Middle East",
        "all_certifications": Certification.objects.filter(status=True),
        "all_brands": Brand.objects.filter(status=True).order_by("sequence"),
        "all_products": homepage_products,
        "all_testimonials": CompanyTestimonial.objects.filter(status=True),
        "display_products": display_products,
    }
    return render(request, "public_interface/home.html", context)


def about(request):
    context = {
        "page_title": "About The Deep Seafood Company | Leading Seafood Supplier in UAE",
        # "about": AboutUs.objects.filter(status=True),
        "management_team": ManagementTeam.objects.filter(status=True),
        "history": History.objects.all(),
    }
    return render(request, "public_interface/about.html", context)


def blog(request):
    context = {
        "page_title": "Seafood Industry Insights & Tips",
    }
    return render(request, "public_interface/blog.html", context)


def blog_details(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    recent_blogs = Blog.objects.filter(status=True).exclude(id=blogs.id).order_by("-id")
    context = {"blog_details": blogs, "recent_blogs": recent_blogs}
    return render(request, "public_interface/blog-view.html", context)


def product(request):
    search = request.GET.get("search")

    if search:
        all_products = Product.objects.filter(
            status=True, name__icontains=search
        ).order_by("sequence")
    else:
        all_products = Product.objects.filter(status=True).order_by("sequence")

    context = {"page_title": "Seafood Products", "all_products": all_products}
    return render(request, "public_interface/products.html", context)


def product_details(request, slug):
    product = get_object_or_404(ProductDetails, slug=slug)
    related_products = (
        Product.objects.filter(status=True)
        .exclude(id=product.product_id)
        .order_by("sequence")
    )
    categories = Category.objects.all()

    context = {
        "product": product,
        "related_products": related_products,
        "categories": categories,
    }

    return render(request, "public_interface/product-view.html", context)


def distribution_channel(request):
    context = {"page_title": "Leading Wholesale Seafood Supplier in UAE"}
    return render(request, "public_interface/distribution.html", context)


def contact(request):
    context = {"page_title": "Contact The Deep Seafood Company"}
    return render(request, "public_interface/contact.html", context)


def career(request):
    context = {
        "page_title": "Careers at The Deep Seafood Company",
        "all_jobs": VacancyDetails.objects.filter(status=True),
        "form": ApplicationDetailsForm(),
    }
    return render(request, "public_interface/career.html", context)


def news_room(request):
    context = {
        "page_title": "Latest News & Updates",
        "all_events": Event.objects.filter(status=True).order_by("sequence")[:3],
        "total_events": Event.objects.filter(status=True).count(),
    }
    return render(request, "public_interface/news-room.html", context)


def news_detail(request, pk):
    news = get_object_or_404(News, id=pk)
    recent_news = News.objects.filter(status=True).exclude(id=news.id)
    context = {"news_detail": news, "recent_news": recent_news}
    return render(request, "public_interface/news-view.html", context)


def brand(request):
    context = {
        "page_title": "Explore oceano",
        "supermarkets": Supermarkets.objects.filter(status=True),
    }
    return render(request, "public_interface/brands.html", context)


def meeting(request):
    return render(request, "meeting.html")


def catalogue(request):
    return render(request, "catalogue.html")


def terms_and_condition(request):
    context = {"page_title": "Terms and Conditions"}

    return render(request, "termsandconditions.html", context)


def privacy_policy(request):
    context = {"page_title": "Privacy Policy"}

    return render(request, "privacy_policy.html", context)


# class IndexView(TemplateView):
#     template_name = "website/index/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         brand = (
#             Brand.objects.filter(status=True)
#             .exclude(name="Deep Sea")
#             .order_by("sequence")
#         )
#         category = Category.objects.filter(status=True).order_by("-id")
#         product = Product.objects.filter(
#             brand__name="Deep Sea", status=True, homepage=True
#         ).order_by("sequence")[:9]
#         blog = Blog.objects.filter(status=True).order_by("-id")
#         testimonial = CompanyTestimonial.objects.filter(status=True).order_by("-id")
#         type = ""
#         certification = Certification.objects.filter(status=True).order_by("-id")

#         context["certification"] = certification
#         context["testimonial"] = testimonial
#         context["type"] = type

#         context["product"] = product
#         context["category"] = category
#         context["brands"] = brand
#         return context


# class ProductView(TemplateView):
#     template_name = "website/products/products.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         type = self.request.GET.get("type")
#         if type:
#             product = Product.objects.filter(
#                 brand__name="Deep Sea", type=type, status=True
#             ).order_by("sequence")
#         else:
#             product = Product.objects.filter(
#                 brand__name="Deep Sea", status=True
#             ).order_by("sequence")
#         blog = Blog.objects.filter(status=True).order_by("-id")
#         # context["data"] = SEO.objects.filter(page="Product").first()
#         context["blog"] = blog
#         context["type"] = type
#         context["product"] = product
#         return context


# class ProductDetailsView(TemplateView):
#     template_name = "website/products/product-view.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug_product = self.kwargs["slug_product"]
#         product = Product.objects.get(slug_product=slug_product)
#         cat = (
#             product.product_details.filter(status=True)
#             .order_by("category__sequence")
#             .values_list("category__id", flat=True)
#             .distinct()
#             .first()
#         )
#         cat_name = (
#             product.product_details.filter(status=True)
#             .order_by("category__sequence")
#             .values_list("category__name", flat=True)
#             .distinct()
#             .first()
#         )
# cat = Category.objects.filter(status=True,brand__name='Deep Sea').order_by('-id').first()
# data = ProductDetails.objects.filter(product=product,category=cat)
# print(data.price)
# try:
#     data = ProductDetails.objects.filter(product=product, category=cat).first()
# except ProductDetails.DoesNotExist:
#     data = None
# list = (
#     Product.objects.filter(status=True, brand__name="Deep Sea")
#     .exclude(slug_product=slug_product)
#     .order_by("sequence")[:6]
# )
# category = Category.objects.filter(
#     status=True, brand__name="Deep Sea"
# ).order_by("sequence")
# blog = Blog.objects.filter(status=True).order_by("-id")
# context["blog"] = blog
# context["category"] = category
# context["cat_name"] = cat_name
# context["cat"] = cat
# context["list"] = list
# context["data"] = data
# context["product"] = product
# return context


# class BlogDetailsView(TemplateView):
#     template_name = "website/blog/blog-view.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs["slug"]
#         data = Blog.objects.get(slug=slug)
#         blog = Blog.objects.filter(status=True).exclude(slug=slug).order_by("-id")
#         # list = BlogDetails.objects.filter(status=True).order_by('-id')
#         # context['blog'] = list
#         context["data"] = data
#         context["blogs"] = blog
#         return context


# class NewsRoomView(TemplateView):
#     template_name = "website/news/news-room.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         gallery = Event.objects.filter(status=True).order_by("sequence")
#         total_events = Event.objects.filter(status=True).count()

#         blog = Blog.objects.filter(status=True).order_by("-id")
#         # context["data"] = SEO.objects.filter(page="News Room").first()
#         context["blog"] = blog
#         context["gallery"] = gallery
#         context["total_events"] = total_events
#         return context


# class NewsDetailsView(TemplateView):
#     template_name = "website/news/news-view.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id = self.kwargs["id"]
#         data = News.objects.get(pk=id)
#         news = News.objects.filter(status=True).exclude(id=id).order_by("-id")
#         # blog = BlogDetails.objects.filter(status=True).order_by('-id')
#         # context['blog'] = blog
#         context["data"] = data
#         context["news"] = news
#         return context


class NewsListsView(TemplateView):
    template_name = "public_interface/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.filter(status=True).order_by("-id")
        context["news"] = news
        return context


class IndexProductView(View):
    template_name = "public_interface/home/product_list.html"

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


class ProductListingView(View):
    template_name = "public_interface/components/products/product_lists.html"

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


class GeneralProductDetailsView(View):
    template_name = "public_interface/components/products/details.html"

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
    template_name = "public_interface/components/products/search_product.html"

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
    template_name = "public_interface/brands.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supermarkets = Supermarkets.objects.filter(status=True).order_by("-id")
        # recipes = RecipeDetails.objects.filter(status=True).order_by("-id")
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
        blog = Blog.objects.filter(status=True).order_by("-id")
        # context["data"] = SEO.objects.filter(page="Oceano").first()
        context["blog"] = blog
        # print(total_product,'***')
        context["category"] = category
        context["total_product"] = total_product
        context["products"] = products
        # context["recipes"] = recipes
        context["supermarkets"] = supermarkets
        return context


class ProductContentView(View):
    template_name = "public_interface/components/brands/products_list.html"

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
    template_name = "public_interface/components/brands/product_details.html"

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
    template_name = "public_interface/components/brands/product_data.html"

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
    template_name = "public_interface/components/brands/brands_list.html"


class BaseAjaxView(View):
    model = None
    template = None
    context_key = "items"
    default_limit = 3
    filters = {}

    def get_queryset(self):
        return self.model.objects.filter(status=True, **self.filters).order_by(
            "sequence"
        )

    def get(self, request):
        if not request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"error": "Invalid request"}, status=400)

        try:
            qs = self.get_queryset()[: self.default_limit]
            context = {self.context_key: qs, "total": self.get_queryset().count()}
            html = render_to_string(self.template, context)
            return JsonResponse(
                {"status": True, "template": html, "total": context["total"]}
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class LoadEvents(BaseAjaxView):
    model = Event
    template = "public_interface/components/news/event_gallery.html"
    context_key = "all_events"


class LoadNews(BaseAjaxView):
    model = News
    template = "public_interface/components/news/news_list.html"
    filters = {"type__iexact": "company news"}


class LoadGlobalNews(LoadNews):
    filters = {"type__iexact": "global news"}


class LoadPromotions(BaseAjaxView):
    model = Promotion
    template = "public_interface/components/news/promotions_list.html"
    default_limit = None


def load_more_news(request):
    return handle_load_more(
        request, News, "public_interface/components/news/loadmore_news.html"
    )


def load_more_events(request):
    return handle_load_more(
        request, Event, "public_interface/components/news/loadmore_events.html"
    )


def handle_load_more(request, model, template_name):
    try:
        params = {
            "offset": int(request.GET.get("offset", 0)),
            "limit": int(request.GET.get("limit", 4)),
            "type": request.GET.get("type", ""),
        }

        filters = {"status": True}
        if params["type"]:
            filters["type__iexact"] = params["type"]

        qs = model.objects.filter(**filters).order_by("sequence")
        items = qs[params["offset"] : params["offset"] + params["limit"]]
        total = qs.count()

        html = render_to_string(
            f"public_interface/components/news/{template_name}",
            {"data": items, "has_more": (params["offset"] + params["limit"]) < total},
        )

        return JsonResponse(
            {"data": html, "has_more": (params["offset"] + params["limit"]) < total}
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


class PromotionView(TemplateView):
    template_name = "public_interface/promotion-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        promotion = Promotion.objects.get(pk=id)
        data = Promotion.objects.filter(status=True).exclude(id=id).order_by("-id")
        context["data"] = data
        context["promotion"] = promotion
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
                contact = ContactUs(
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
                enquiry = Enquiry(
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
        honey = request.POST.get("honey")
        if honey:
            messages.error(request, "Error: Form submission not allowed.")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        # Create mutable copies
        adjusted_post = request.POST.copy()
        adjusted_files = request.FILES.copy()

        # Map field names to match form
        field_mappings = {
            "applied": "job",
            "phone": "phone_number",
            "linkedin": "linkedin_url",
            "portfolio": "portfolio_url",
            "date": "date_of_birth",
            "attachment": "upload_cv",
            "cover": "cover_letter",
        }

        for old_name, new_name in field_mappings.items():
            if old_name in adjusted_post:
                adjusted_post[new_name] = adjusted_post[old_name]
            if old_name in adjusted_files:
                adjusted_files[new_name] = adjusted_files[old_name]

        form = ApplicationDetailsForm(adjusted_post, adjusted_files)

        if form.is_valid():
            application = form.save(commit=False)

            # Prepare email
            email = EmailMessage(
                "New Form Submission-Deep Seafood Company Website",
                self._build_email_body(form.cleaned_data),
                "deepseafood.connect@gmail.com",
                ["info@thedeepseafood.com"],
            )

            self._attach_files(email, form)
            email.send()
            application.save()

            messages.success(request, "Your Request Shared Successfully")
        else:
            self._handle_form_errors(request, form)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    def _build_email_body(self, cleaned_data):
        return f"""First Name: {cleaned_data['first_name']}
                Last Name: {cleaned_data['last_name']}
                Date Of Birth: {cleaned_data['date_of_birth']}
                Mobile: {cleaned_data['phone_number']}
                Email: {cleaned_data['email']}
                Notice Period: {cleaned_data['notice_period']}
                Portfolio: {cleaned_data['portfolio_url']}
                LinkedIn: {cleaned_data['linkedin_url']}
                Message: {cleaned_data.get('message', '')}"""

    def _attach_files(self, email, form):
        for field in ["upload_cv", "cover_letter"]:
            if file := form.cleaned_data.get(field):
                email.attach(file.name, file.read(), file.content_type)

    def _handle_form_errors(self, request, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{form.fields[field].label}: {error}")
