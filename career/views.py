from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from career.models import JobCategory, VaccancyDetails, ApplicationDetails
from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q

from django.contrib import messages
# from deepapp.helper import is_ajax, renderhelper
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template import loader


class JobCategoryListView(TemplateView):
    template_name = "superadmin/job category/job_category_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "JobCategory"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = JobCategory.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                JobCategory.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = JobCategory.objects.get(id=item_id)
                except JobCategory.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "job category", "job_category_view", context)


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


class CareerListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Career"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = VaccancyDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(title__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                VaccancyDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = VaccancyDetails.objects.get(id=item_id)
                except VaccancyDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "career", "career_view", context)


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


class ApplicationListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/application/application_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "application"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        start_date = request.GET.get("start_date")  # Get start_date from request
        end_date = request.GET.get("end_date")  # Get end_date from request

        cd = ApplicationDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(
                    Q(first_name__icontains=search) | Q(job__icontains=search)
                )
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                ApplicationDetails.objects.filter(id=item_id).update(status=status)

            if start_date and end_date:  # Filter by date range if provided
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                cd = cd.filter(date__range=(start_date, end_date))

            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ApplicationDetails.objects.get(id=item_id)
                except ApplicationDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "application", "application_view", context)
