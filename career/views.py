from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from career.models import JobCategory, VacancyDetails, ApplicationDetails
from career.forms import VacancyDetailForm, JobCategoryForm

# from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

# from django.http import JsonResponse
from company.mixin import StatusUpdateAndDeleteMixin, SearchAndStatusFilterMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import SuperuserOrAdminRequiredMixin, SuperAdminOrHrRequiredMixin


class JobCategoryListView(
    LoginRequiredMixin,
    SuperAdminOrHrRequiredMixin,
    StatusUpdateAndDeleteMixin,
    SearchAndStatusFilterMixin,
    ListView,
):
    model = JobCategory
    context_object_name = "all_job_category"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/job category/job_category_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Job Category",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("job_category_add"),
    }


class JobCategoryCreateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, CreateView
):
    model = JobCategory
    form_class = JobCategoryForm
    success_url = reverse_lazy("job_category_view")
    template_name = "superadmin/job category/job_category_create.html"
    extra_context = {
        "page_title": "Job Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("job_category_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Job Category Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class JobCategoryUpdateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, UpdateView
):
    model = JobCategory
    form_class = JobCategoryForm
    success_url = reverse_lazy("job_category_view")
    template_name = "superadmin/job category/job_category_create.html"
    extra_context = {
        "page_title": "Job Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("job_category_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Job Category Updated Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CareerListView(
    LoginRequiredMixin,
    SuperAdminOrHrRequiredMixin,
    StatusUpdateAndDeleteMixin,
    SearchAndStatusFilterMixin,
    ListView,
):
    model = VacancyDetails
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_vacancy"
    template_name = "superadmin/career/career_view.html"
    search_field = "title"
    extra_context = {
        "page_title": "Career",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("career_add"),
    }


class CareerCreateView(LoginRequiredMixin, SuperAdminOrHrRequiredMixin, CreateView):
    model = VacancyDetails
    success_url = reverse_lazy("career_view")
    form_class = VacancyDetailForm
    template_name = "superadmin/career/career_create.html"
    extra_context = {
        "page_title": "Career",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("career_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Career Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CareerUpdateView(LoginRequiredMixin, SuperAdminOrHrRequiredMixin, UpdateView):
    model = VacancyDetails
    success_url = reverse_lazy("career_view")
    form_class = VacancyDetailForm
    template_name = "superadmin/career/career_create.html"
    extra_context = {
        "page_title": "Career",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("career_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Career Update Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class ApplicationListView(
    LoginRequiredMixin,
    SuperAdminOrHrRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):  # TODO need to filter wise date
    model = ApplicationDetails
    context_object_name = "all_applications"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/application/application_view.html"
    search_field = "job"
    search_field = "start_date"
    extra_context = {"page_title": "Application", "status": True, "search_date": True}
