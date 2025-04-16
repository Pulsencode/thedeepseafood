# from django.shortcuts import render
from django.urls import reverse_lazy
from company.models import CompanyTestimonial, AboutUs, ManagementTeam
from company.forms import CompanyTestimonialForm, AboutUsForm, ManagementTeamForm
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages


class CompanyTestimonialListView(ListView):
    model = CompanyTestimonial
    context_object_name = "all_testimonials"
    template_name = "company/list_testimonial.html"


class CompanyTestimonialCreateView(CreateView):
    model = CompanyTestimonial
    template_name = "create_update.html"
    form_class = CompanyTestimonialForm
    success_url = reverse_lazy("view_company_testimonial")
    extra_context = {
        "page_title": "Create Testimonial",
    }

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Added Successfully...!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CompanyTestimonialUpdateView(UpdateView):
    model = CompanyTestimonial
    form_class = CompanyTestimonial
    template_name = "create_update.html"
    success_url = reverse_lazy("view_company_testimonial")
    extra_context = {
        "page_title": "Update Testimonial",
    }

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# About
class AboutListView(ListView):
    model = AboutUs
    template_name = "company/list_about.html"
    context_object_name = "all_about"


class AboutCreateView(CreateView):
    model = AboutUs
    template_name = "create_update.html"
    form_class = AboutUsForm
    success_url = reverse_lazy("view_about_us")
    extra_context = {
        "page_title": "Create About Us",
    }

    def form_valid(self, form):
        messages.success(self.request, "About Us Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class AboutUpdateView(UpdateView):
    model = AboutUs
    template_name = "create_update.html"
    form_class = AboutUsForm
    success_url = reverse_lazy("view_about_us")
    extra_context = {
        "page_title": "Update About Us",
    }

    def form_valid(self, form):
        messages.success(self.request, "About Us Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# Team Member


class TeamListView(ListView):
    model = ManagementTeam
    template_name = "company/list_team_member.html"
    context_object_name = "all_team_member"


class TeamCreateView(CreateView):
    model = ManagementTeam
    template_name = "create_update.html"
    form_class = ManagementTeamForm
    success_url = reverse_lazy("view_team")
    extra_context = {
        "page_title": "Create Team",
    }

    def form_valid(self, form):
        messages.success(self.request, "Team Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TeamUpdateView(UpdateView):
    model = ManagementTeam
    template_name = "create_update.html"
    form_class = ManagementTeamForm
    success_url = reverse_lazy("view_team")
    extra_context = {
        "page_title": "Update Team",
    }

    def form_valid(self, form):
        messages.success(self.request, "Team Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)
