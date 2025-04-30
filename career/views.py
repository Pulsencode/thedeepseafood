from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from career.models import JobCategory, VaccancyDetails, ApplicationDetails

# from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib import messages

# from deepapp.helper import is_ajax, renderhelper
# from django.http import JsonResponse
from company.mixin import StatusUpdateMixin, SearchAndStatusFilterMixin


class JobCategoryListView(StatusUpdateMixin, SearchAndStatusFilterMixin, ListView):
    model = JobCategory
    context_object_name = "all_job_category"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/job category/job_category_view.html"
    search_field = "name"


class JobCategoryCreateView(TemplateView):
    template_name = "superadmin/job category/job_category_create.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        jcategory = JobCategory(name=name)
        jcategory.save()
        messages.success(request, "Job category Added Successfully...!!")
        return redirect("job_category_view")


class JobCategoryUpdateView(TemplateView):
    template_name = "superadmin/job category/job_category_create.html"

    def get(self, request, id):
        data = JobCategory.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = JobCategory.objects.get(pk=id)
        name = request.POST.get("name")

        data.name = name
        data.save()
        messages.success(request, "Job Category Updated Successfully...!!")
        return redirect("job_category_view")


class CareerListView(StatusUpdateMixin, SearchAndStatusFilterMixin, ListView):
    model = VaccancyDetails
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_vacancy"
    template_name = "superadmin/career/career_view.html"
    search_field = "title"


class CareerCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def post(self, request, *args, **kwargs):
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        location = request.POST.get("location")
        salary = request.POST.get("salary")
        # cat_instance = request.POST.get('cat')
        # category = JobCategory.objects.get(id=cat_instance)
        types = request.POST.getlist("types")
        types_str = ", ".join(types)

        career = VaccancyDetails(
            salary=salary,
            type=types_str,
            title=name,
            description=desc,
            location=location,
        )
        career.save()

        messages.success(request, "Career Added Successfully...!!")
        return redirect("career_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = JobCategory.objects.filter(status=True).order_by("-id")
        return context


class CareerUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, id):
        data = VaccancyDetails.objects.get(pk=id)
        types_list = data.type.split(", ")
        # category = JobCategory.objects.filter(status=True)
        return render(
            request, self.template_name, {"list": data, "types_list": types_list}
        )

    def post(self, request, id):
        data = VaccancyDetails.objects.get(pk=id)
        # category = JobCategory.objects.filter(status=True)
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        location = request.POST.get("location")
        salary = request.POST.get("salary")
        # cat_instance = request.POST.get('cat')
        # category = JobCategory.objects.get(id=cat_instance)

        types = request.POST.getlist("types")

        data.type = ", ".join(types)
        data.title = name
        # data.category = category
        data.location = location
        data.salary = salary
        data.description = desc
        data.save()
        messages.success(request, "Career Updated Successfully...!!")
        return redirect("career_view")


class ApplicationListView(
    SearchAndStatusFilterMixin, ListView
):  # TODO need to filter wise date
    model = ApplicationDetails
    context_object_name = "all_applications"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/application/application_view.html"
    search_field = "job"
