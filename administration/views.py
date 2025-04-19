from django.shortcuts import redirect
from django.views.generic import TemplateView
from company.models import (
    BlogDetails,
    Brand,
    CompanyTestimonial,
    ContactUsDetails,
    EnquiryDetails,
    EventGallery,
    HistoryDetails,
    ManagementTeam,
    NewsDetails,
    PromotionDetails,
)
from django.contrib import messages

from career.models import ApplicationDetails, JobCategory, VaccancyDetails
from products.models import RecipeDetails, Product, Category
from django.contrib.auth import authenticate, login


class IndexView(TemplateView):
    template_name = "superadmin/index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = Brand.objects.filter(status=True).order_by("-id").count()
        category = Category.objects.filter(status=True).order_by("-id").count()
        job = JobCategory.objects.filter(status=True).order_by("-id").count()
        recipe = RecipeDetails.objects.filter(status=True).order_by("-id").count()
        gallery = EventGallery.objects.filter(status=True).order_by("-id").count()
        news = NewsDetails.objects.filter(status=True).order_by("-id").count()
        promo = PromotionDetails.objects.filter(status=True).order_by("-id").count()
        blog = BlogDetails.objects.filter(status=True).order_by("-id").count()
        team = ManagementTeam.objects.filter(status=True).order_by("-id").count()
        testi = CompanyTestimonial.objects.filter(status=True).order_by("-id").count()
        career = VaccancyDetails.objects.filter(status=True).order_by("-id").count()
        appli = ApplicationDetails.objects.filter(status=True).order_by("-id").count()
        history = HistoryDetails.objects.filter(status=True).order_by("-id").count()
        contact = ContactUsDetails.objects.filter().order_by("-id").count()
        enquiry = EnquiryDetails.objects.filter().order_by("-id").count()
        product = Product.objects.filter().order_by("-id").count()
        context["product"] = product
        context["enquiry"] = enquiry
        context["contact"] = contact
        context["history"] = history
        context["appli"] = appli
        context["career"] = career
        context["testi"] = testi
        context["team"] = team
        context["blog"] = blog
        context["promo"] = promo
        context["news"] = news
        context["gallery"] = gallery
        context["recipe"] = recipe
        context["job"] = job
        context["category"] = category
        context["brand"] = brand
        return context


class LoginView(TemplateView):
    template_name = "superadmin/login/login.html"

    def post(self, request, *args, **kwargs):
        uname = self.request.POST.get("uname")
        password = self.request.POST.get("pass")
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect("index_view")
            else:
                messages.error(request, "You are not a verified user")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login_view")
