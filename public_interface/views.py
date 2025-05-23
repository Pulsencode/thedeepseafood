import logging

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from career.forms import ApplicationDetailsForm
from career.models import VacancyDetails
from company.forms import EnquiryForm, ProductEnquiryForm
from company.models import (
    Blog,
    Brand,
    Certification,
    CompanyTestimonial,
    Event,
    History,
    ManagementTeam,
    News,
    Promotion,
    Supermarkets,
)
from products.models import Category, Product, ProductDetails, Subcategory


def home(request):
    selected_type = request.GET.get("type")

    products = Product.objects.filter(status=True, homepage=True).order_by("sequence")

    if selected_type:
        products = products.filter(type=selected_type)
    else:
        products = products[:9]

    context = {
        "all_products": products,
        "page_title": "Wholesale Seafood Export & Import Supplier in UAE, Middle East",
        "all_certifications": Certification.objects.filter(status=True),
        "all_brands": Brand.objects.filter(status=True).order_by("sequence"),
        "all_testimonials": CompanyTestimonial.objects.filter(status=True),
        "view_more_button": True,
    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string(
            "public_interface/components/products/product_lists.html", context
        )
        return JsonResponse({"html": html})

    return render(request, "public_interface/home.html", context)


def about(request):
    context = {
        "page_title": "About The Deep Seafood Company | Leading Seafood Supplier in UAE",
        "management_team": ManagementTeam.objects.filter(status=True),
        "history": History.objects.all(),
        "form": EnquiryForm(),
        "action_url": reverse("enquiry"),
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
    selected_type = request.GET.get("type")

    products = Product.objects.filter(status=True)

    if selected_type:
        products = products.filter(type=selected_type)

    if search:
        products = products.filter(name__icontains=search)

    products = products.order_by("sequence")

    context = {
        "all_products": products,
        "page_title": "Seafood Products",
    }

    # AJAX request handling
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string(
            "public_interface/components/products/product_lists.html", context
        )
        return JsonResponse({"html": html})

    return render(request, "public_interface/products.html", context)


def product_details(request, slug):
    product = get_object_or_404(ProductDetails, slug=slug)
    related_products = (
        Product.objects.filter(status=True)
        .exclude(id=product.product_id)
        .order_by("sequence")[:6]
    )
    categories = Category.objects.all()
    sub_categories = Subcategory.objects.all()

    context = {
        "product": product,
        "related_products": related_products,
        "categories": categories,
        "sub_categories": sub_categories,
        "form": ProductEnquiryForm(),
        "action_url": reverse("product_enquiry"),
    }

    return render(request, "public_interface/product-view.html", context)


def distribution_channel(request):
    context = {"page_title": "Leading Wholesale Seafood Supplier in UAE"}
    return render(request, "public_interface/distribution.html", context)


def contact(request):
    context = {
        "page_title": "Contact The Deep Seafood Company",
        "form": EnquiryForm,
    }
    return render(request, "public_interface/contact.html", context)


def career(request):
    all_jobs = VacancyDetails.objects.filter(status=True)
    unique_locations = VacancyDetails.objects.values_list(
        "location", flat=True
    ).distinct()

    unique_titles = VacancyDetails.objects.values_list("title", flat=True).distinct()

    if request.method == "GET":
        job_title = request.GET.get("job_title")
        location = request.GET.get("location")
        job_type = request.GET.get("job_type")

        if job_title:
            all_jobs = all_jobs.filter(title__icontains=job_title)
        if location:
            all_jobs = all_jobs.filter(location__icontains=location)
        if job_type:
            all_jobs = all_jobs.filter(type__icontains=job_type)

    context = {
        "page_title": "Careers at The Deep Seafood Company",
        "all_jobs": all_jobs,
        "form": ApplicationDetailsForm(),
        "unique_locations": unique_locations,
        "unique_titles": unique_titles,
    }
    return render(request, "public_interface/career.html", context)


def job_application(request):

    if request.method == "POST":
        job_id = request.POST.get("job_id")
        job = get_object_or_404(VacancyDetails, id=job_id)

        form = ApplicationDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = job

            application.save()
            messages.success(request, "Application  Submitted successfully ")
            return redirect("career")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.success(request, errors)
            return redirect("career")


def news_room(request):
    news_type = request.GET.get("news_type")
    all_news = None
    all_events = None
    limit = 3

    if news_type:
        all_news = News.objects.filter(status=True, type=news_type).order_by(
            "sequence"
        )[:limit]
        total = News.objects.filter(status=True, type=news_type).count()
    else:
        all_events = Event.objects.filter(status=True).order_by("sequence")
        total = 0
    context = {
        "all_news": all_news,
        "all_events": all_events,
        "total_events": Event.objects.filter(status=True).count(),
        "page_title": "Latest News & Updates",
        "show_load_more": total > limit,
        "limit": limit,
        "total": total,
        "news_type": news_type,
    }

    return render(request, "public_interface/news-room.html", context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
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
    return render(request, "termsandconditions.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


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


logger = logging.getLogger(__name__)


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

    def get_context_data(self, **kwargs):
        context = {
            self.context_key: self.get_queryset()[: self.default_limit],
            "total": self.get_queryset().count(),
        }
        return context

    def get(self, request):
        if not request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"error": "Invalid request"}, status=400)

        try:
            context = self.get_context_data()
            html = render_to_string(self.template, context)
            return JsonResponse(
                {"status": True, "template": html, "total": context["total"]}
            )
        except Exception as e:
            logger.error(f"Error in {self.__class__.__name__}: {str(e)}", exc_info=True)
            return JsonResponse({"error": "Server error"}, status=500)


def load_more_news(request):
    offset = int(request.GET.get("offset", 0))
    limit = int(request.GET.get("limit", 3))
    news_type = request.GET.get("news_type")

    news_qs = News.objects.filter(status=True).order_by("sequence")
    if news_type:
        news_qs = news_qs.filter(type=news_type)

    total = news_qs.count()
    news_qs = news_qs[offset : offset + limit]

    html = render_to_string(
        "public_interface/components/news/news_list.html", {"all_news": news_qs}
    )
    return JsonResponse({"html": html, "has_more": offset + limit < total})


class LoadPromotions(BaseAjaxView):
    model = Promotion
    template = "public_interface/components/news/promotions_list.html"
    default_limit = None


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


def enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {"message": "Enquiry Submitted Successfully", "status": "success"}
            )
        else:
            errors = []
            for error_list in form.errors.values():
                for error in error_list:
                    errors.append(error)
            return JsonResponse(
                {
                    "message": errors[0] if errors else "Invalid form data",
                    "status": "error",
                },
                status=400,
            )

    return JsonResponse(
        {"message": "Error when submitting", "status": "error"}, status=400
    )


def product_enquiry(request):
    if request.method == "POST":
        product_slug = request.POST.get("product_slug")
        product = get_object_or_404(ProductDetails, slug=product_slug)
        form = ProductEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.product = product
            enquiry.save()
            return JsonResponse(
                {"message": "Enquiry Submitted Successfully", "status": "success"}
            )
        else:
            errors = []
            for error_list in form.errors.values():
                for error in error_list:
                    errors.append(error)
            return JsonResponse(
                {
                    "message": errors[0] if errors else "Invalid form data",
                    "status": "error",
                },
                status=400,
            )

    return JsonResponse(
        {"message": "Error when submitting", "status": "error"}, status=400
    )
