from django.shortcuts import redirect
from django.views.generic import TemplateView
from company.models import (
    Blog,
    Brand,
    CompanyTestimonial,
    ContactUs,
    Enquiry,
    Event,
    History,
    ManagementTeam,
    News,
    Promotion,
)
from django.contrib import messages

from career.models import ApplicationDetails, JobCategory, VacancyDetails
from products.models import Product, Category
from django.contrib.auth import authenticate, login


class AdminDashboardView(TemplateView):
    template_name = "administration/pages/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        models_to_count = {
            "brand": Brand,
            "category": Category,
            "job": JobCategory,
            "gallery": Event,
            "news": News,
            "promo": Promotion,
            "blog": Blog,
            "team": ManagementTeam,
            "testimonials": CompanyTestimonial,
            "career": VacancyDetails,
            "application": ApplicationDetails,
            "history": History,
            "contact": ContactUs,
            "enquiry": Enquiry,
            "product": Product,
        }

        for context_key, model_class in models_to_count.items():
            if hasattr(model_class, "status"):
                count = model_class.objects.filter(status=True).count()
            else:
                count = model_class.objects.all().count()
            context[context_key] = count

        return context


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def post(self, request, *args, **kwargs):
        uname = self.request.POST.get("uname")
        password = self.request.POST.get("pass")
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect("admin_dashboard")
            else:
                messages.error(request, "You are not a verified user")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login_view")
