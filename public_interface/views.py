from django.shortcuts import render, redirect
from company.models import (
    Certification,
    Supermarkets,
    AboutUs,
    HistoryImage,
    ManagementTeam,
    Brand,
    BlogDetails,
    CompanyTestimonial,
    NewsDetails,
    EventGallery,
)
from django.shortcuts import get_object_or_404
from products.models import Product, ProductDetails
from django.contrib import messages
from career.models import JobPosting
from public_interface.forms import JobApplicationForm


def home(request):
    all_products = Product.objects.all().order_by("sequence")
    homepage_products = Product.objects.filter(homepage=True).order_by("sequence")[:9]

    # If no homepage marked, show the first 9 of all products
    if not homepage_products:
        display_products = all_products[:9]
    else:
        display_products = homepage_products

    context = {
        "page_title": "Home",
        "all_certifications": Certification.objects.filter(status=True),
        "all_brands": Brand.objects.filter(status=True).order_by("sequence"),
        "all_products": homepage_products,
        "all_testimonials": CompanyTestimonial.objects.filter(status=True),
        "display_products": display_products,
    }
    return render(request, "public_interface/home.html", context)


def about(request):
    context = {
        "page_title": "About",
        "about": AboutUs.objects.filter(status=True),
        "management_team": ManagementTeam.objects.filter(status=True),
        "history": HistoryImage.objects.all(),
    }
    return render(request, "public_interface/about.html", context)


def product(request):
    context = {
        "page_title": "Product",
        "all_products": Product.objects.filter(status=True),
    }
    return render(request, "public_interface/products.html", context)


def product_details(request, slug):
    product = get_object_or_404(ProductDetails, slug=slug)
    related_products = (
        Product.objects.filter(status=True).exclude(id=product.id).order_by("sequence")
    )

    context = {"product": product, "related_products": related_products}

    return render(request, "public_interface/details.html", context)


def career(request):

    context = {
        "page_title": "Careers at The Deep Seafood Company",
        "all_jobs": JobPosting.objects.filter(status=True),
        "forms": JobApplicationForm,
    }
    return render(request, "public_interface/career.html", context)


def apply_job(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Job Application Successfully submit")
            return redirect("career")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors)
            return redirect("career")

    context = {"page_title": "Careers at The Deep Seafood Company"}
    return render(request, "public_interface/career.html", context)



def contact(request):
    context = {"page_title": "Contact The Deep Seafood Company"}
    return render(request, "public_interface/contact.html", context)


def blogs(request):
    context = {
        "page_title": "Company Blog",
        "blog": BlogDetails.objects.filter(status=True),
    }
    return render(request, "public_interface/blog.html", context)


def blog_details(request, slug):
    blog = get_object_or_404(BlogDetails, slug=slug)
    recent_blog = (
        BlogDetails.objects.filter(status=True).exclude(id=blog.id).order_by("-date")
    )

    context = {"detail_blog": blog, "recent_blog": recent_blog}
    return render(request, "public_interface/blog.html", context)


def distribution_channel(request):
    context = {"page_title": "Leading Wholesale Seafood Supplier in UAE"}
    return render(request, "public_interface/distribution.html", context)


def news_room(request):
    context = {
        "page_title": "Latest News & update",
        "all_news": NewsDetails.objects.filter(status=True),
        "all_events": EventGallery.objects.filter(status=True),
    }
    return render(request, "public_interface/news_room.html", context)


def news_detail(request, slug):
    news = get_object_or_404(NewsDetails, slug=slug)
    recent_news = (
        NewsDetails.objects.filter(status=True).exclude(id=news.id).order_by("-id")
    )
    context = {"news_detail": news, "recent_news": recent_news}
    return render(request, "news_details.html", context)


def brand(request):
    context = {
        "page_title": "Explore oceano",
        "supermarkets": Supermarkets.objects.filter(status=True),
    }
    return render(request, "public_interface/oceano.html", context)


def terms_and_condition(request):
    context = {"page_title": "Terms and Conditions"}

    return render(request, "public_interface/terms_condition.html", context)


def privacy_policy(request):
    context = {"page_title": "Privacy Policy"}

    return render(request, "public_interface/privacy.html", context)
