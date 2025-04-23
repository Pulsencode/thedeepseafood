from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView
from deepapp.helper import is_ajax, renderhelper
from datetime import datetime

from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from django.core.files.base import ContentFile
# import base64
from company.forms import (
    SEOForm,
    ManagementForm,
    TestimonialForm,
    CertificationForm,
    SupermarketForm,
    BrandForm,
    BlogForm,
    BlogImageFormSet,
)
from company.models import (
    # AboutUs,
    Blog,
    BlogImage,
    Brand,
    Certification,
    CompanyTestimonial,
    ContactUs,
    Enquiry,
    Event,
    EventImage,
    History,
    HistoryImage,
    ManagementTeam,
    News,
    NewsImage,
    Promotion,
    PromotionImage,
    SEO,
    Supermarkets,
)


class SeoListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/seo/seo-list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "seo"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = SEO.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(page__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                SEO.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = SEO.objects.get(id=item_id)
                except SEO.DoesNotExist:
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
        return renderhelper(request, "seo", "seo-view", context)


class SeoCreateView(CreateView):
    model = SEO
    form_class = SEOForm
    template_name = "superadmin/seo/seo-create.html"
    extra_context = {"page_title": "Create SEO"}
    success_url = reverse_lazy("list_seo")

    def form_valid(self, form):
        messages.success(self.request, "Seo Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class SeoUpdateView(UpdateView):
    model = SEO
    form_class = SEOForm
    template_name = "superadmin/seo/seo-create.html"
    extra_context = {"page_title": "Update SEO"}
    success_url = reverse_lazy("list_seo")

    def form_valid(self, form):
        messages.success(self.request, "Seo Updated Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TeamListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/team/management_team_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Team"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = ManagementTeam.objects.all().order_by("-id")

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
                ManagementTeam.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ManagementTeam.objects.get(id=item_id)
                except ManagementTeam.DoesNotExist:
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

        return renderhelper(request, "team", "management_team_view", context)


class TeamCreateView(CreateView):
    model = ManagementTeam
    form_class = ManagementForm
    success_url = reverse_lazy("list_team")
    template_name = "superadmin/team/management_team_create.html"
    extra_context = {"page_title": "Create Team"}

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
    form_class = ManagementForm
    success_url = reverse_lazy("list_team")
    template_name = "superadmin/team/management_team_create.html"
    extra_context = {"page_title": "Update Team"}

    def form_valid(self, form):
        messages.success(self.request, "Team Updated  Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TestimonialListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/testimonial/testimonial_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Testimonial"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = CompanyTestimonial.objects.all().order_by("-id")

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
                CompanyTestimonial.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = CompanyTestimonial.objects.get(id=item_id)
                except CompanyTestimonial.DoesNotExist:
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

        return renderhelper(request, "testimonial", "testimonial_view", context)


class TestimonialCreateView(CreateView):
    model = CompanyTestimonial
    form_class = TestimonialForm
    success_url = reverse_lazy("list_testimonial")
    template_name = "superadmin/testimonial/testimonial_create.html"
    extra_context = {"page_title": "Create Testimonial"}

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TestimonialUpdateView(UpdateView):
    model = CompanyTestimonial
    form_class = TestimonialForm
    success_url = reverse_lazy("list_testimonial")
    template_name = "superadmin/testimonial/testimonial_create.html"
    extra_context = {"page_title": "Update Testimonial"}

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CertificationListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/certification/certification_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "certification"
        page = request.GET.get("page", 1)

        # search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Certification.objects.all().order_by("-id")

        if is_ajax(request):
            # if search:
            #     cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Certification.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Certification.objects.get(id=item_id)
                except Certification.DoesNotExist:
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
        return renderhelper(request, "certification", "certification_view", context)


class CertificationCreateView(CreateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    template_name = "superadmin/certification/certification_create.html"
    extra_context = {"page_title": "Create Certification"}

    def form_valid(self, form):
        messages.success(self.request, "Certification Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class CertificationUpdateView(UpdateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    template_name = "superadmin/certification/certification_create.html"
    extra_context = {"page_title": "Update Certification"}

    def form_valid(self, form):
        messages.success(self.request, "Certification Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class SupermarketListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/supermarket/supermarket_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "supermarket"
        page = request.GET.get("page", 1)

        # search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Supermarkets.objects.all().order_by("-id")

        if is_ajax(request):
            # if search:
            #     cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Supermarkets.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Supermarkets.objects.get(id=item_id)
                except Supermarkets.DoesNotExist:
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
        return renderhelper(request, "supermarket", "supermarket_view", context)


class SupermarketCreateView(CreateView):
    template_name = "superadmin/supermarket/supermarket_create.html"
    model = Supermarkets
    form_class = SupermarketForm
    success_url = reverse_lazy("list_supermarket")
    extra_context = {"page_title": "Create Supermarket"}

    def form_valid(self, form):
        messages.success(self.request, "Supermarket Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class SupermarketUpdateView(UpdateView):
    template_name = "superadmin/supermarket/supermarket_create.html"
    model = Supermarkets
    form_class = SupermarketForm
    success_url = reverse_lazy("list_supermarket")
    extra_context = {"page_title": "Create Supermarket"}

    def form_valid(self, form):
        messages.success(self.request, "Supermarket Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class BrandListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand/brand_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Brand"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Brand.objects.exclude(name="Deep Sea").order_by("-id")

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
                Brand.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Brand.objects.get(id=item_id)
                except Brand.DoesNotExist:
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
        # print(cd)
        return renderhelper(request, "brand", "brand_view", context)


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy("brand_view")
    success_url = reverse_lazy("list_brand")
    template_name = "superadmin/brand/brand_create.html"

    def form_valid(self, form):
        messages.success(self.request, "Brand Created Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class BrandUpdateView(UpdateView):

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy("brand_view")
    # success_url=reverse_lazy("list_brand")
    template_name = "superadmin/brand/brand_create.html"

    def form_valid(self, form):
        messages.success(self.request, "Brand Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


######################################


class GalleryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Event Gallery"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Event.objects.all().order_by("-id")

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
                Event.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Event.objects.get(id=item_id)
                except Event.DoesNotExist:
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

        return renderhelper(request, "event gallery", "event_gallery_view", context)


class GalleryCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        # name = request.POST.get('name')
        location = request.POST.get("location")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        gallery = Event(
            title=title,
            location=location,
            description=desc,
            date=date,
            sequence=sequence,
            image_alt=image_alt,
        )
        gallery.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = Event(event=gallery, image=image)
            slider.save()
        messages.success(request, "Gallery Added Successfully...!!")
        return redirect("gallery_view")


class GalleryUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Event.objects.get(pk=id)
        sliders = data.gallery_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = Event.objects.get(pk=id)
        # sliders = data.gallery_image.all()
        title = request.POST.get("title")
        # name = request.POST.get('name')
        location = request.POST.get("location")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        # data.name = name
        data.location = location
        data.sequence = sequence
        data.description = desc
        data.image_alt = image_alt
        data.date = date
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = Event(event=data, image=image)
            slider.save()
        messages.success(request, "Gallery Updated Successfully...!!")
        return redirect("gallery_view")


def delete_slider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = Event.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class NewsListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "News"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = News.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                News.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = News.objects.get(id=item_id)
                except News.DoesNotExist:
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

        return renderhelper(request, "news", "news_view", context)


class NewsCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        type = request.POST.get("type")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")

        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        news = News(
            sequence=sequence,
            title=title,
            name=name,
            location=location,
            description=desc,
            date=date,
            type=type,
            image_alt=image_alt,
            title_tag=title_tag,
            # metatag=metatag,
            # keyword=keyword,
            # canonical=canonical,
        )
        news.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = News(news=news, image=image)
            slider.save()
        messages.success(request, "News Added Successfully...!!")
        return redirect("news_view")


class NewsUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = News.objects.get(pk=id)
        sliders = data.news_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = News.objects.get(pk=id)
        # sliders = data.news_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        type = request.POST.get("type")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.sequence = sequence
        data.type = type
        data.location = location
        data.description = desc
        data.date = date
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = News(news=data, image=image)
            slider.save()
        messages.success(request, "News Updated Successfully...!!")
        return redirect("news_view")


def delete_newsslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = NewsImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class PromotionListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Promotion"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Promotion.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Promotion.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Promotion.objects.get(id=item_id)
                except Promotion.DoesNotExist:
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

        return renderhelper(request, "promotion", "promotion_info_view", context)


class PromotionCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        promotion = Promotion(
            title=title, name=name, location=location, description=desc, date=date
        )
        promotion.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = PromotionImage(promotion=promotion, image=image)
            slider.save()
        messages.success(request, "Promotion Added Successfully...!!")
        return redirect("promotion_view")


class PromotionUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Promotion.objects.get(pk=id)
        sliders = data.promo_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = Promotion.objects.get(pk=id)
        # sliders = data.promo_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.location = location
        data.description = desc
        data.date = date
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = PromotionImage(promotion=data, image=image)
            slider.save()
        messages.success(request, "Promotion Updated Successfully...!!")
        return redirect("promotion_view")


def delete_promotionslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = PromotionImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class BlogListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/blog/Blog_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Blog"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Blog.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Blog.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Blog.objects.get(id=item_id)
                except Blog.DoesNotExist:
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

        return renderhelper(request, "blog", "Blog_view", context)


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "superadmin/blog/Blog_create.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["image_formset"] = BlogImageFormSet(
                self.request.POST, self.request.FILES
            )
        else:
            data["image_formset"] = BlogImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context["image_formset"]

        # Save Blog first
        self.object = form.save(commit=False)
        self.object.save()

        # Set instance BEFORE validating formset
        image_formset.instance = self.object
        if image_formset.is_valid():
            image_formset.save()
            return redirect("blog_view")
        else:
            return self.render_to_response(self.get_context_data(form=form))


class BlogUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/blog/Blog_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Blog.objects.get(pk=id)
        sliders = data.blog_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = Blog.objects.get(pk=id)
        # sliders = data.blog_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.location = location
        data.description = desc
        data.date = date
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = BlogImage(blog=data, image=image)
            slider.save()
        messages.success(request, "Blog Updated Successfully...!!")
        return redirect("blog_view")


def delete_blogslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = BlogImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class HistoryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "History"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = History.objects.all().order_by("-id")

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
                History.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = History.objects.get(id=item_id)
                except History.DoesNotExist:
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

        return renderhelper(request, "history", "history_view", context)


class HistoryCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        year = request.POST.get("year")
        desc = request.POST.get("desc")
        image_alt = request.POST.get("image_alt")

        history = History(title=title, year=year, description=desc, image_alt=image_alt)
        history.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = HistoryImage(history=history, image=image)
            slider.save()
        messages.success(request, "History Added Successfully...!!")
        return redirect("history_view")


class HistoryUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = History.objects.get(pk=id)
        sliders = data.history_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = History.objects.get(pk=id)
        # sliders = data.history_image.all()
        title = request.POST.get("title")
        year = request.POST.get("year")
        desc = request.POST.get("desc")
        image_alt = request.POST.get("image_alt")

        data.title = title
        data.year = year
        data.description = desc
        data.image_alt = image_alt
        data.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = HistoryImage(history=data, image=image)
            slider.save()
        messages.success(request, "History Updated Successfully...!!")
        return redirect("history_view")


def delete_historyslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = HistoryImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class ContactListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/contact/contact_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Contat"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        # status = request.GET.get("status")
        # sts = request.GET.get("sts")

        cd = ContactUs.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ContactUs.objects.get(id=item_id)
                except ContactUs.DoesNotExist:
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

        return renderhelper(request, "contact", "contact_view", context)


class EnquiryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/enquiry/enquiry_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Enquiry"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        # status = request.GET.get("status")
        # sts = request.GET.get("sts")
        start = request.GET.get("start")
        end = request.GET.get("end")
        start_date = None
        end_date = None

        if start and end:
            start_date = datetime.strptime(start, "%m/%d/%Y").date()
            end_date = datetime.strptime(end, "%m/%d/%Y").date()

        cd = Enquiry.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(
                    Q(name__icontains=search) | Q(created__range=(start, end))
                )
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Enquiry.objects.get(id=item_id)
                except Enquiry.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            if start_date and end_date:
                cd = cd.filter(
                    created__date__gte=start_date, created__date__lte=end_date
                )

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

        return renderhelper(request, "enquiry", "enquiry", context)


class ExportExcel(View):
    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            start = request.GET.get("start")
            end = request.GET.get("end")

            try:
                enquiries = Enquiry.objects.filter(created__gte=start, created__lte=end)
                enquiries_data = [
                    {
                        "product": enquiry.product,
                        "name": enquiry.name,
                        "location": enquiry.location,
                        "email": enquiry.email,
                        "mobile_no": enquiry.mobile_no,
                        "message": enquiry.message,
                        "created": enquiry.created.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for enquiry in enquiries
                ]
                return JsonResponse({"status": True, "enquiries": enquiries_data})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


# class AboutusListView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/aboutus/aboutus_list.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "aboutus"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         cd = AboutUs.objects.all().order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(title__icontains=search)
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 AboutUs.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = AboutUs.objects.get(id=item_id)
#                 except AboutUs.DoesNotExist:
#                     datas = None
#                 if datas:
#                     datas.delete()

#             paginator = Paginator(cd, 10)
#             try:
#                 datas = paginator.get_page(page)
#             except PageNotAnInteger:
#                 datas = paginator.get_page(1)
#             except EmptyPage:
#                 datas = paginator.get_page(paginator.num_pages)
#             context["datas"] = datas
#             context["page"] = page
#             template = loader.get_template(self.template_name)
#             html_content = template.render(context, request)
#             return JsonResponse({"status": True, "template": html_content})

#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         context["path"] = path
#         return renderhelper(request, "aboutus", "aboutus_view", context)


# class AboutusCreateView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/aboutus/aboutus_create.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def post(self, request, *args, **kwargs):
#         image = request.FILES.get("image")
#         title = request.POST.get("title")

#         about = AboutUs(image=image, title=title)
#         about.save()
#         messages.success(request, "About Us Added Successfully...!!")
#         return redirect("about_view")


# class AboutusUpdateView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/aboutus/aboutus_create.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, id):
#         data = AboutUs.objects.get(pk=id)
#         return render(request, self.template_name, {"list": data})

#     def post(self, request, id):
#         data = AboutUs.objects.get(pk=id)
#         image = request.FILES.get("image")
#         title = request.POST.get("title")

#         if image:
#             data.image = image
#         data.title = title
#         data.save()

#         messages.success(request, "About Us Updated Successfully...!!")
#         return redirect("about_view")
