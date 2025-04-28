# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    # TemplateView,
    View,
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
)

# from deepapp.helper import is_ajax, renderhelper
# from datetime import datetime


# from deepapp.helper import is_ajax, renderhelper
# from datetime import datetime

# from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse

# from django.shortcuts import redirect, render
# from django.template import loader
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.core.files.base import ContentFile
import base64
from company.forms import (
    HistoryForm,
    NewsForm,
    SEOForm,
    ManagementForm,
    TestimonialForm,
    CertificationForm,
    SupermarketForm,
    BrandForm,
    BlogForm,
    EventForm,
    PromotionForm,
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
from company.mixin import SearchStatusMixin, StatusMixin


# def status(request, pk):
#     if request.method == "POST":
#         seo_list = get_object_or_404(SEO, id=pk)
#         status = request.POST.get("status", "")
#         seo_list.status = status == "on"
#         seo_list.save()
#         return redirect("list_seo")


class SeoListView(SearchStatusMixin, StatusMixin, ListView):
    model = SEO
    context_object_name = "all_seo"
    paginate_by = 10
    template_name = "superadmin/seo/seo-view.html"
    search_field = "page_name"

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    # path = "seo"
    # page = request.GET.get("page", 1)

    # search = request.GET.get("search")
    # delete = request.GET.get("delete")
    # status = request.GET.get("status")
    # sts = request.GET.get("sts")

    # # cd = SEO.objects.all().order_by("-id")

    # if is_ajax(request):
    #     if search:
    #         cd = cd.filter(page__icontains=search)
    #     if sts:
    #         cd = cd.filter(status=sts)
    #     if status:
    #         if status == "1":
    #             status = True
    #         else:
    #             status = False
    #         item_id = request.GET.get("item_id")
    #         SEO.objects.filter(id=item_id).update(status=status)
    #     if delete:
    #         item_id = request.GET.get("item_id")
    #         try:
    #             datas = SEO.objects.get(id=item_id)
    #         except SEO.DoesNotExist:
    #             datas = None
    #         if datas:
    #             datas.delete()

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     # context["datas"] = datas
    #     context["page"] = page
    #     template = loader.get_template(self.template_name)
    #     html_content = template.render(context, request)
    #     return JsonResponse({"status": True, "template": html_content})


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


class TeamListView(SearchStatusMixin, StatusMixin, ListView):
    model = ManagementTeam
    paginate_by = 10
    context_object_name = "all_teams"
    template_name = "superadmin/team/management_team_view.html"
    search_field = "role"


# class TeamListView(UserPassesTestMixin, TemplateView):
# template_name = "superadmin/team/management_team_view.html"

# def test_func(self):
#     return self.request.user.username == "DeepSeaAdmin"

# def get(self, request, *args, **kwargs):
#     context = {}
#     path = "Team"
#     page = request.GET.get("page", 1)

#     search = request.GET.get("search")
#     delete = request.GET.get("delete")
#     status = request.GET.get("status")
#     sts = request.GET.get("sts")

#     cd = ManagementTeam.objects.all().order_by("-id")

#     if is_ajax(request):
#         if search:
#             cd = cd.filter(name__icontains=search)
#         if sts:
#             cd = cd.filter(status=sts)
#         if status:
#             if status == "1":
#                 status = True
#             else:
#                 status = False
#             item_id = request.GET.get("item_id")
#             ManagementTeam.objects.filter(id=item_id).update(status=status)
#         if delete:
#             item_id = request.GET.get("item_id")
#             try:
#                 datas = ManagementTeam.objects.get(id=item_id)
#             except ManagementTeam.DoesNotExist:
#                 datas = None
#             if datas:
#                 datas.delete()
#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         template = loader.get_template(self.template_name)
#         html_content = template.render(context, request)
#         return JsonResponse({"status": True, "template": html_content})

#     paginator = Paginator(cd, 10)
#     try:
#         datas = paginator.get_page(page)
#     except PageNotAnInteger:
#         datas = paginator.get_page(1)
#     except EmptyPage:
#         datas = paginator.get_page(paginator.num_pages)
#     context["datas"] = datas
#     context["page"] = page
#     context["path"] = path

#     return renderhelper(request, "team", "management_team_view", context)


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


class TestimonialListView(SearchStatusMixin, StatusMixin, ListView):
    model = CompanyTestimonial
    paginated_by = 10
    context_object_name = "all_testimonials"
    template_name = "superadmin/testimonial/testimonial_view.html"
    search_field = "name"


# class TestimonialListView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/testimonial/testimonial_list.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Testimonial"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         cd = CompanyTestimonial.objects.all().order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(name__icontains=search)
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 CompanyTestimonial.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = CompanyTestimonial.objects.get(id=item_id)
#                 except CompanyTestimonial.DoesNotExist:
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

#         return renderhelper(request, "testimonial", "testimonial_view", context)


class TestimonialCreateView(CreateView):
    model = CompanyTestimonial
    form_class = TestimonialForm
    success_url = reverse_lazy("list_testimonial")
    template_name = "superadmin/testimonial/testimonial_create.html"

    def form_valid(self, form):
        # Handle cropped image
        cropped_image = self.request.POST.get("testi-image")
        if cropped_image:
            # Convert base64 to Django file
            format, imgstr = cropped_image.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f"cropped.{ext}")
            form.instance.image = data

        messages.success(self.request, "Testimonial Added Successfully...!!")
        return super().form_valid(form)


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


class CertificationListView(SearchStatusMixin, StatusMixin, ListView):
    model = Certification
    context_object_name = "all_certification"
    paginate_by = 10
    template_name = "superadmin/certification/certification_view.html"

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     path = "certification"
    #     page = request.GET.get("page", 1)

    #     # search = request.GET.get("search")
    #     delete = request.GET.get("delete")
    #     status = request.GET.get("status")
    #     sts = request.GET.get("sts")

    #     cd = Certification.objects.all().order_by("-id")

    #     if is_ajax(request):
    #         # if search:
    #         #     cd = cd.filter(name__icontains=search)
    #         if sts:
    #             cd = cd.filter(status=sts)
    #         if status:
    #             if status == "1":
    #                 status = True
    #             else:
    #                 status = False
    #             item_id = request.GET.get("item_id")
    #             Certification.objects.filter(id=item_id).update(status=status)
    #         if delete:
    #             item_id = request.GET.get("item_id")
    #             try:
    #                 datas = Certification.objects.get(id=item_id)
    #             except Certification.DoesNotExist:
    #                 datas = None
    #             if datas:
    #                 datas.delete()

    #         paginator = Paginator(cd, 10)
    #         try:
    #             datas = paginator.get_page(page)
    #         except PageNotAnInteger:
    #             datas = paginator.get_page(1)
    #         except EmptyPage:
    #             datas = paginator.get_page(paginator.num_pages)
    #         context["datas"] = datas
    #         context["page"] = page
    #         template = loader.get_template(self.template_name)
    #         html_content = template.render(context, request)
    #         return JsonResponse({"status": True, "template": html_content})

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     context["datas"] = datas
    #     context["page"] = page
    #     context["path"] = path
    #     return renderhelper(request, "certification", "certification_view", context)


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


class SupermarketListView(SearchStatusMixin, StatusMixin, ListView):
    model = Supermarkets
    context_object_name = "all_supermarkets"
    paginate_by = 10
    template_name = "superadmin/supermarket/supermarket_view.html"


# class SupermarketListView(UserPassesTestMixin, TemplateView):

# template_name = "superadmin/supermarket/supermarket_list.html"

# def test_func(self):
#     return self.request.user.username == "DeepSeaAdmin"

# def get(self, request, *args, **kwargs):
#     context = {}
#     path = "supermarket"
#     page = request.GET.get("page", 1)

#     # search = request.GET.get("search")
#     delete = request.GET.get("delete")
#     status = request.GET.get("status")
#     sts = request.GET.get("sts")

#     cd = Supermarkets.objects.all().order_by("-id")

#     if is_ajax(request):
#         # if search:
#         #     cd = cd.filter(name__icontains=search)
#         if sts:
#             cd = cd.filter(status=sts)
#         if status:
#             if status == "1":
#                 status = True
#             else:
#                 status = False
#             item_id = request.GET.get("item_id")
#             Supermarkets.objects.filter(id=item_id).update(status=status)
#         if delete:
#             item_id = request.GET.get("item_id")
#             try:
#                 datas = Supermarkets.objects.get(id=item_id)
#             except Supermarkets.DoesNotExist:
#                 datas = None
#             if datas:
#                 datas.delete()

#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         template = loader.get_template(self.template_name)
#         html_content = template.render(context, request)
#         return JsonResponse({"status": True, "template": html_content})

#     paginator = Paginator(cd, 10)
#     try:
#         datas = paginator.get_page(page)
#     except PageNotAnInteger:
#         datas = paginator.get_page(1)
#     except EmptyPage:
#         datas = paginator.get_page(paginator.num_pages)
#     context["datas"] = datas
#     context["page"] = page
#     context["path"] = path
#     return renderhelper(request, "supermarket", "supermarket_view", context)


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


class BrandListView(SearchStatusMixin, StatusMixin, ListView):
    model = Brand
    context_object_name = "all_brands"
    paginate_by = 10
    template_name = "superadmin/brand/brand_view.html"
    search_field = "name"

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     path = "Brand"
    #     page = request.GET.get("page", 1)

    #     search = request.GET.get("search")
    #     delete = request.GET.get("delete")
    #     status = request.GET.get("status")
    #     sts = request.GET.get("sts")

    #     cd = Brand.objects.exclude(name="Deep Sea").order_by("-id")

    #     if is_ajax(request):
    #         if search:
    #             cd = cd.filter(name__icontains=search)
    #         if sts:
    #             cd = cd.filter(status=sts)
    #         if status:
    #             if status == "1":
    #                 status = True
    #             else:
    #                 status = False
    #             item_id = request.GET.get("item_id")
    #             Brand.objects.filter(id=item_id).update(status=status)
    #         if delete:
    #             item_id = request.GET.get("item_id")
    #             try:
    #                 datas = Brand.objects.get(id=item_id)
    #             except Brand.DoesNotExist:
    #                 datas = None
    #             if datas:
    #                 datas.delete()
    #         paginator = Paginator(cd, 10)
    #         try:
    #             datas = paginator.get_page(page)
    #         except PageNotAnInteger:
    #             datas = paginator.get_page(1)
    #         except EmptyPage:
    #             datas = paginator.get_page(paginator.num_pages)
    #         context["datas"] = datas
    #         context["page"] = page
    #         template = loader.get_template(self.template_name)
    #         html_content = template.render(context, request)
    #         return JsonResponse({"status": True, "template": html_content})

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     context["datas"] = datas
    #     context["page"] = page
    #     context["path"] = path
    #     # print(cd)
    #     return renderhelper(request, "brand", "brand_view", context)


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


class BlogListView(SearchStatusMixin, StatusMixin, ListView):
    model = Blog
    context_object_name = "all_blogs"
    paginated_by = 10
    template_name = "superadmin/blog/Blog_view.html"
    search_field = "name"


# class BlogListView(UserPassesTestMixin, ListView):
#     template_name = "superadmin/blog/Blog_view.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Blog"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         cd = Blog.objects.all().order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 Blog.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = Blog.objects.get(id=item_id)
#                 except Blog.DoesNotExist:
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

#         return renderhelper(request, "blog", "Blog_view", context)


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "superadmin/blog/Blog_create.html"
    success_url = reverse_lazy("blog_view")

    def form_valid(self, form):
        self.object = form.save()

        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["id_image_alt"]
        for image in images:
            BlogImage.objects.create(blog=self.object, image=image, image_alt=image_alt)
        messages.success(self.request, "Blog Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog_view")
    template_name = "superadmin/blog/Blog_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.blog_image.all()

        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["id_image_alt"]

        for image in images:
            BlogImage.objects.create(blog=self.object, image=image, image_alt=image_alt)
        messages.success(self.request, "Blog Updated  Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class EventListView(SearchStatusMixin, StatusMixin, ListView):
    model = Event
    context_object_name = "all_events"
    paginate_by = 10
    template_name = "superadmin/event gallery/event_gallery_view.html"
    search_field = "name"


# class EventListView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/event gallery/event_gallery_list.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Event Gallery"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         cd = Event.objects.all().order_by("-id")

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
#                 Event.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = Event.objects.get(id=item_id)
#                 except Event.DoesNotExist:
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

#         return renderhelper(request, "event gallery", "event_gallery_view", context)


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("gallery_view")
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")

        for image in images:
            EventImage.objects.create(event=self.object, image=image)

        messages.success(self.request, "Event Created Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("gallery_view")
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.event_image.all()

        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")

        for image in images:
            EventImage.objects.create(event=self.object, image=image)

        messages.success(self.request, "Event Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# def delete_slider(request, image_id):
#     try:
#         # Get the image by its ID and delete it
#         image = Event.objects.get(pk=image_id)
#         image.image.delete()  # Delete the image file
#         image.delete()  # Delete the database record
#         return JsonResponse({"success": True})
#     except EventImage.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Image not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)}, status=500)
class EventImageDelete(DeleteView):
    model = EventImage
    success_url = reverse_lazy("gallery_view")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class NewsListView(SearchStatusMixin, StatusMixin, ListView):
    model = News
    context_object_name = "all_news"
    paginate_by = 10
    template_name = "superadmin/news/news_view.html"
    search_field = "name"


# class NewsListView(UserPassesTestMixin, TemplateView):
#     template_name = "superadmin/news/news_list.html"

#     def test_func(self):
#         return self.request.user.username == "DeepSeaAdmin"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "News"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         cd = News.objects.all().order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 News.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = News.objects.get(id=item_id)
#                 except News.DoesNotExist:
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

#         return renderhelper(request, "news", "news_view", context)


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("news_view")
    template_name = "superadmin/news/news_create.html"

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            NewsImage.objects.create(news=self.object, image=image)
        messages.success(self.request, "News Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("news_view")
    template_name = "superadmin/news/news_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.news_image.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            NewsImage.objects.create(news=self.object, image=image)
        messages.success(self.request, "News Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# def delete_newsslider(request, image_id):
#     try:
#         # Get the image by its ID and delete it
#         image = NewsImage.objects.get(pk=image_id)
#         image.image.delete()  # Delete the image file
#         image.delete()  # Delete the database record
#         return JsonResponse({"success": True})
#     except EventImage.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Image not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)}, status=500)
class NewsImageDelete(DeleteView):
    model = NewsImage
    success_url = reverse_lazy("news_view")

    def get(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class PromotionListView(SearchStatusMixin, StatusMixin, ListView):
    model = Promotion
    context_object_name = "all_promotions"
    paginate_by = 10
    template_name = "superadmin/promotion/promotion_info_view.html"
    search_field = "name"


# promotion listview
# def test_func(self):
#     return self.request.user.username == "DeepSeaAdmin"

# def get(self, request, *args, **kwargs):
#     context = {}
#     path = "Promotion"
#     page = request.GET.get("page", 1)

#     search = request.GET.get("search")
#     delete = request.GET.get("delete")
#     status = request.GET.get("status")
#     sts = request.GET.get("sts")

#     cd = Promotion.objects.all().order_by("-id")

#     if is_ajax(request):
#         if search:
#             cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
#         if sts:
#             cd = cd.filter(status=sts)
#         if status:
#             if status == "1":
#                 status = True
#             else:
#                 status = False
#             item_id = request.GET.get("item_id")
#             Promotion.objects.filter(id=item_id).update(status=status)
#         if delete:
#             item_id = request.GET.get("item_id")
#             try:
#                 datas = Promotion.objects.get(id=item_id)
#             except Promotion.DoesNotExist:
#                 datas = None
#             if datas:
#                 datas.delete()
#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         template = loader.get_template(self.template_name)
#         html_content = template.render(context, request)
#         return JsonResponse({"status": True, "template": html_content})

#     paginator = Paginator(cd, 10)
#     try:
#         datas = paginator.get_page(page)
#     except PageNotAnInteger:
#         datas = paginator.get_page(1)
#     except EmptyPage:
#         datas = paginator.get_page(paginator.num_pages)
#     context["datas"] = datas
#     context["page"] = page
#     context["path"] = path

#     return renderhelper(request, "promotion", "promotion_info_view", context)


class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = "superadmin/promotion/promotion_info_create.html"
    success_url = reverse_lazy("promotion_view")

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            PromotionImage.objects.create(promotion=self.object, image=image)
        messages.success(self.request, "Promotion Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):

        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = "superadmin/promotion/promotion_info_create.html"
    success_url = reverse_lazy("promotion_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.promotion_image.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            PromotionImage.objects.create(promotion=self.object, image=image)
        messages.success(self.request, "Promotion Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):

        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# def delete_promotionslider(request, image_id):
#     try:
#         # Get the image by its ID and delete it
#         image = PromotionImage.objects.get(pk=image_id)
#         image.image.delete()  # Delete the image file
#         image.delete()  # Delete the database record
#         return JsonResponse({"success": True})
#     except EventImage.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Image not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)}, status=500)
class PromotionImageDelete(DeleteView):
    model = PromotionImage
    success_url = reverse_lazy("promotion_view")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class BlogImageDelete(DeleteView):
    model = BlogImage
    success_url = reverse_lazy("blog_view")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class HistoryListView(SearchStatusMixin, StatusMixin, ListView):
    model = History
    context_object_name = "all_history"
    paginate_by = 10
    template_name = "superadmin/history/history_view.html"
    search_field = "year"
    # history View

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     path = "History"
    #     page = request.GET.get("page", 1)

    #     search = request.GET.get("search")
    #     delete = request.GET.get("delete")
    #     status = request.GET.get("status")
    #     sts = request.GET.get("sts")

    #     cd = History.objects.all().order_by("-id")

    #     if is_ajax(request):
    #         if search:
    #             cd = cd.filter(title__icontains=search)
    #         if sts:
    #             cd = cd.filter(status=sts)
    #         if status:
    #             if status == "1":
    #                 status = True
    #             else:
    #                 status = False
    #             item_id = request.GET.get("item_id")
    #             History.objects.filter(id=item_id).update(status=status)
    #         if delete:
    #             item_id = request.GET.get("item_id")
    #             try:
    #                 datas = History.objects.get(id=item_id)
    #             except History.DoesNotExist:
    #                 datas = None
    #             if datas:
    #                 datas.delete()
    #         paginator = Paginator(cd, 10)
    #         try:
    #             datas = paginator.get_page(page)
    #         except PageNotAnInteger:
    #             datas = paginator.get_page(1)
    #         except EmptyPage:
    #             datas = paginator.get_page(paginator.num_pages)
    #         context["datas"] = datas
    #         context["page"] = page
    #         template = loader.get_template(self.template_name)
    #         html_content = template.render(context, request)
    #         return JsonResponse({"status": True, "template": html_content})

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     context["datas"] = datas
    #     context["page"] = page
    #     context["path"] = path

    #     return renderhelper(request, "history", "history_view", context)


class HistoryCreateView(CreateView):
    model = History
    form_class = HistoryForm
    template_name = "superadmin/history/history_create.html"
    success_url = reverse_lazy("history_view")

    def form_valid(self, form):
        self.objects = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            HistoryImage.objects.create(history=self.objects, image=image)
        messages.success(self.request, "History Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class HistoryUpdateView(UpdateView):
    model = History
    form_class = HistoryForm
    template_name = "superadmin/history/history_create.html"
    success_url = reverse_lazy("history_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.history_image.all()
        return context

    def form_valid(self, form):
        self.objects = form.save()
        images = self.request.FILES.getlist("images")
        for image in images:
            HistoryImage.objects.create(history=self.objects, image=image)
        messages.success(self.request, "History Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


# def delete_historyslider(request, image_id):
#     try:
#         # Get the image by its ID and delete it
#         image = HistoryImage.objects.get(pk=image_id)
#         image.image.delete()  # Delete the image file
#         image.delete()  # Delete the database record
#         return JsonResponse({"success": True})
#     except EventImage.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Image not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)}, status=500)


class HistoryImageDelete(DeleteView):
    model = HistoryImage
    success_url = reverse_lazy("history_view")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ContactListView(SearchStatusMixin, StatusMixin, ListView):
    model = ContactUs
    context_object_name = "all_contacts"
    paginate_by = 10
    template_name = "superadmin/contact/contact_view.html"
    search_field = "name"

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     path = "Contat"
    #     page = request.GET.get("page", 1)

    #     search = request.GET.get("search")
    #     delete = request.GET.get("delete")
    # status = request.GET.get("status")
    # sts = request.GET.get("sts")

    # cd = ContactUs.objects.all().order_by("-id")

    # if is_ajax(request):
    #     if search:
    #         cd = cd.filter(name__icontains=search)
    #     if delete:
    #         item_id = request.GET.get("item_id")
    #         try:
    #             datas = ContactUs.objects.get(id=item_id)
    #         except ContactUs.DoesNotExist:
    #             datas = None
    #         if datas:
    #             datas.delete()

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     context["datas"] = datas
    #     context["page"] = page
    #     template = loader.get_template(self.template_name)
    #     html_content = template.render(context, request)
    #     return JsonResponse({"status": True, "template": html_content})

    # paginator = Paginator(cd, 10)
    # try:
    #     datas = paginator.get_page(page)
    # except PageNotAnInteger:
    #     datas = paginator.get_page(1)
    # except EmptyPage:
    #     datas = paginator.get_page(paginator.num_pages)
    # context["datas"] = datas
    # context["page"] = page
    # context["path"] = path

    # return renderhelper(request, "contact", "contact_view", context)


class EnquiryListView(SearchStatusMixin, StatusMixin, ListView):
    model = Enquiry
    context_object_name = "all_enquiry"
    paginate_by = 10
    template_name = "superadmin/enquiry/enquiry_view.html"
    search_field = "year"

    # def test_func(self):
    #     return self.request.user.username == "DeepSeaAdmin"

    # def get(self, request, *args, **kwargs):
    #     context = {}
    #     path = "Enquiry"
    #     page = request.GET.get("page", 1)

    #     search = request.GET.get("search")
    #     delete = request.GET.get("delete")
    #     # status = request.GET.get("status")
    #     # sts = request.GET.get("sts")
    #     start = request.GET.get("start")
    #     end = request.GET.get("end")
    #     start_date = None
    #     end_date = None

    #     if start and end:
    #         start_date = datetime.strptime(start, "%m/%d/%Y").date()
    #         end_date = datetime.strptime(end, "%m/%d/%Y").date()

    #     cd = Enquiry.objects.all().order_by("-id")

    #     if is_ajax(request):
    #         if search:
    #             cd = cd.filter(
    #                 Q(name__icontains=search) | Q(created__range=(start, end))
    #             )
    #         if delete:
    #             item_id = request.GET.get("item_id")
    #             try:
    #                 datas = Enquiry.objects.get(id=item_id)
    #             except Enquiry.DoesNotExist:
    #                 datas = None
    #             if datas:
    #                 datas.delete()

    #         if start_date and end_date:
    #             cd = cd.filter(
    #                 created__date__gte=start_date, created__date__lte=end_date
    #             )

    #         paginator = Paginator(cd, 10)
    #         try:
    #             datas = paginator.get_page(page)
    #         except PageNotAnInteger:
    #             datas = paginator.get_page(1)
    #         except EmptyPage:
    #             datas = paginator.get_page(paginator.num_pages)
    #         context["datas"] = datas
    #         context["page"] = page
    #         template = loader.get_template(self.template_name)
    #         html_content = template.render(context, request)
    #         return JsonResponse({"status": True, "template": html_content})

    #     paginator = Paginator(cd, 10)
    #     try:
    #         datas = paginator.get_page(page)
    #     except PageNotAnInteger:
    #         datas = paginator.get_page(1)
    #     except EmptyPage:
    #         datas = paginator.get_page(paginator.num_pages)
    #     context["datas"] = datas
    #     context["page"] = page
    #     context["path"] = path

    #     return renderhelper(request, "enquiry", "enquiry", context)


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
