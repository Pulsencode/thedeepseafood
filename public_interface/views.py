from django.shortcuts import render


def home(request):
    context = {"page_title": "Home"}
    return render(request, "public_interface/home.html", context)


def about(request):
    context = {"page_title": "About"}
    return render(request, "public_interface/about.html", context)


def product(request):
    context = {"page_title": "Product"}
    return render(request, "public_interface/products.html", context)


def product_details(request, slug):
    return render(request, "public_interface/about.html")


def career(request):
    context = {"page_title": "Careers at The Deep Seafood Company"}
    return render(request, "public_interface/about.html", context)


def contact(request):
    context = {"page_title": "Contact The Deep Seafood Company"}
    return render(request, "public_interface/contact.html", context)


def blogs(request):
    context = {"page_title": "Company Blog"}
    return render(request, "public_interface/blog.html", context)


def blog_details(request, slug):
    return render(request, "public_interface/blog.html")


def distribution_channel(request):
    context = {"page_title": "Leading Wholesale Seafood Supplier in UAE"}
    return render(request, "public_interface/distribution_channel.html", context)


def news_room(request):
    context = {"page_title": "Latest News & update"}
    return render(request, "public_interface/news_room.html", context)


def brand(request):
    context = {"page_title": "Explore oceano"}
    return render(request, "public_interface/about.html", context)


def terms_and_condition(request):
    context = {"page_title": "Terms and Conditions"}

    return render(request, "public_interface/terms_condition.html", context)


def privacy_policy(request):
    context = {"page_title": "Privacy Policy"}

    return render(request, "public_interface/privacy.html", context)
