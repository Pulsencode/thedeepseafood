from django.urls import reverse_lazy
from django.views.generic import (
    # TemplateView,
    View,
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
)
from django.contrib import messages
from django.http import JsonResponse
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
from company.mixin import (
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import SuperuserOrAdminRequiredMixin


class SeoListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = SEO
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_seo"
    template_name = "superadmin/seo/seo-view.html"
    search_field = "page_name"
    extra_context = {
        "page_title": "SEO",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("seo_add"),
    }


class SeoCreateView(LoginRequiredMixin, CreateView):
    model = SEO
    form_class = SEOForm
    template_name = "superadmin/seo/seo-create.html"
    success_url = reverse_lazy("list_seo")
    extra_context = {
        "page_title": "SEO",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_seo"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Seo Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class SeoUpdateView(LoginRequiredMixin, UpdateView):
    model = SEO
    form_class = SEOForm
    template_name = "superadmin/seo/seo-create.html"
    extra_context = {"page_title": "Update SEO"}
    success_url = reverse_lazy("list_seo")
    extra_context = {
        "page_title": "SEO",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_seo"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Seo Updated Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TeamListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = ManagementTeam
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_teams"
    template_name = "superadmin/team/management_team_view.html"
    search_field = "role"
    extra_context = {
        "page_title": "Management Team",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("team_add"),
    }


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = ManagementTeam
    form_class = ManagementForm
    success_url = reverse_lazy("list_team")
    template_name = "superadmin/team/management_team_create.html"
    extra_context = {
        "page_title": "Management Team",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_team"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Team Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = ManagementTeam
    form_class = ManagementForm
    success_url = reverse_lazy("list_team")
    template_name = "superadmin/team/management_team_create.html"
    extra_context = {
        "page_title": "Management Team",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_team"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, "Team Updated  Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TestimonialListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = CompanyTestimonial
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_testimonials"
    template_name = "superadmin/testimonial/testimonial_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Testimonial",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("testimonial_add"),
    }


class TestimonialCreateView(LoginRequiredMixin, CreateView):
    model = CompanyTestimonial
    form_class = TestimonialForm
    success_url = reverse_lazy("list_testimonial")
    template_name = "superadmin/testimonial/testimonial_create.html"
    extra_context = {
        "page_title": "Testimonial",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_testimonial"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TestimonialUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyTestimonial
    form_class = TestimonialForm
    success_url = reverse_lazy("list_testimonial")
    template_name = "superadmin/testimonial/testimonial_create.html"
    extra_context = {
        "page_title": "Testimonial",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_testimonial"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CertificationListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Certification
    context_object_name = "all_certification"
    paginate_by = 10
    ordering = ["-id"]

    template_name = "superadmin/certification/certification_view.html"
    extra_context = {
        "page_title": "Certification",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("certification_add"),
        "search": True,
    }


class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    template_name = "superadmin/certification/certification_create.html"
    extra_context = {
        "page_title": "Certification",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_certification"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Certification Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class CertificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    template_name = "superadmin/certification/certification_create.html"
    extra_context = {
        "page_title": "Certification",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_certification"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certification"] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, "Certification Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class SupermarketListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Supermarkets
    context_object_name = "all_supermarkets"
    paginate_by = 10
    ordering = ["-id"]

    template_name = "superadmin/supermarket/supermarket_view.html"
    extra_context = {
        "page_title": "Supermarkets",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("supermarket_add"),
    }


class SupermarketCreateView(CreateView):
    template_name = "superadmin/supermarket/supermarket_create.html"
    model = Supermarkets
    form_class = SupermarketForm
    success_url = reverse_lazy("list_supermarket")
    extra_context = {
        "page_title": "Supermarkets",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_supermarket"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Supermarket Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class SupermarketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "superadmin/supermarket/supermarket_create.html"
    model = Supermarkets
    form_class = SupermarketForm
    success_url = reverse_lazy("list_supermarket")
    extra_context = {
        "page_title": "Supermarkets",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("list_supermarket"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supermarkets"] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, "Supermarket Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class BrandListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Brand
    context_object_name = "all_brands"
    paginate_by = 10
    ordering = ["-id"]

    template_name = "superadmin/brand/brand_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Brand",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("brand_add"),
    }


class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy("brand_view")
    template_name = "superadmin/brand/brand_create.html"
    extra_context = {
        "page_title": "Brand",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("brand_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Brand Created Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class BrandUpdateView(LoginRequiredMixin, UpdateView):

    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy("brand_view")
    template_name = "superadmin/brand/brand_create.html"
    extra_context = {
        "page_title": "Brand",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("brand_view"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = self.object
        return context

    def form_valid(self, form):
        messages.success(self.request, "Brand Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class BlogListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Blog
    context_object_name = "all_blogs"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/blog/Blog_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Blog",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("blog_add"),
    }


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "superadmin/blog/Blog_create.html"
    success_url = reverse_lazy("blog_view")
    extra_context = {
        "page_title": "Blog",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("blog_view"),
    }

    def form_valid(self, form):
        self.object = form.save()

        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]
        for image in images:
            BlogImage.objects.create(blog=self.object, image=image, image_alt=image_alt)
        messages.success(self.request, "Blog Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog_view")
    template_name = "superadmin/blog/Blog_create.html"
    extra_context = {
        "page_title": "Blog",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("blog_view"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.blog_image.all()

        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            BlogImage.objects.create(blog=self.object, image=image, image_alt=image_alt)

        self.object.blog_image.update(image_alt=image_alt)
        messages.success(self.request, "Blog Updated  Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class BlogImageDelete(LoginRequiredMixin, DeleteView):
    model = BlogImage

    def get_success_url(self):
        return reverse_lazy("blog_update", kwargs={"pk": self.object.blog.pk})

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class EventListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Event
    context_object_name = "all_events"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/event gallery/event_gallery_view.html"
    search_field = "name"

    extra_context = {
        "page_title": "Event Gallery",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("gallery_add"),
    }


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("gallery_view")
    template_name = "superadmin/event gallery/event_gallery_create.html"

    extra_context = {
        "page_title": "Event Gallery",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("gallery_view"),
    }

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            EventImage.objects.create(
                event=self.object, image=image, image_alt=image_alt
            )

        messages.success(self.request, "Event Created Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("gallery_view")
    template_name = "superadmin/event gallery/event_gallery_create.html"
    extra_context = {
        "page_title": "Event Gallery",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("gallery_view"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.event_image.all()

        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            EventImage.objects.create(
                event=self.object, image=image, image_alt=image_alt
            )
        self.object.event_image.update(image_alt=image_alt)
        messages.success(self.request, "Event Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class EventImageDelete(LoginRequiredMixin, DeleteView):
    model = EventImage

    def get_success_url(self):
        return reverse_lazy("gallery_update", kwargs={"pk": self.object.event.pk})

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class NewsListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = News
    context_object_name = "all_news"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/news/news_view.html"
    search_field = "name"

    extra_context = {
        "page_title": "News",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("news_add"),
    }


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("news_view")
    template_name = "superadmin/news/news_create.html"
    extra_context = {
        "page_title": "News",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("news_view"),
    }

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            NewsImage.objects.create(news=self.object, image=image, image_alt=image_alt)
        messages.success(self.request, "News Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("news_view")
    template_name = "superadmin/news/news_create.html"
    extra_context = {
        "page_title": "News",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("news_view"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.news_image.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            NewsImage.objects.create(news=self.object, image=image, image_alt=image_alt)
        self.object.news_image.update(image_alt=image_alt)
        messages.success(self.request, "News Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class NewsImageDelete(LoginRequiredMixin, DeleteView):
    model = NewsImage

    def get_success_url(self):
        return reverse_lazy("news_update", kwargs={"pk": self.object.news.pk})

    def get(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class PromotionListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Promotion
    context_object_name = "all_promotions"
    paginate_by = 10
    ordering = ["-id"]

    template_name = "superadmin/promotion/promotion_info_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Promotion information",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("promotion_add"),
    }


class PromotionCreateView(LoginRequiredMixin, CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = "superadmin/promotion/promotion_info_create.html"
    success_url = reverse_lazy("promotion_view")
    extra_context = {
        "page_title": "Promotion information",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("promotion_view"),
    }

    def form_valid(self, form):
        self.object = form.save()
        images = self.request.FILES.getlist("images")
        # image_alt = self.request.POST["image_alt"]

        for image in images:
            PromotionImage.objects.create(
                promotion=self.object,
                image=image,
            )
        messages.success(self.request, "Promotion Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):

        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class PromotionUpdateView(LoginRequiredMixin, UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = "superadmin/promotion/promotion_info_create.html"
    success_url = reverse_lazy("promotion_view")
    extra_context = {
        "page_title": "Promotion information",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("promotion_view"),
    }

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


class PromotionImageDelete(LoginRequiredMixin, DeleteView):
    model = PromotionImage

    def get_success_url(self):
        return reverse_lazy("promotion_update", kwargs={"pk": self.object.promotion.pk})

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class HistoryListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = History
    context_object_name = "all_history"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/history/history_view.html"
    search_field = "year"
    extra_context = {
        "page_title": "History",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("history_add"),
    }


class HistoryCreateView(LoginRequiredMixin, CreateView):
    model = History
    form_class = HistoryForm
    template_name = "superadmin/history/history_create.html"
    success_url = reverse_lazy("history_view")
    extra_context = {
        "page_title": "History",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("history_view"),
    }

    def form_valid(self, form):
        self.objects = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST["image_alt"]

        for image in images:
            HistoryImage.objects.create(
                history=self.objects, image=image, image_alt=image_alt
            )
        messages.success(self.request, "History Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class HistoryUpdateView(LoginRequiredMixin, UpdateView):
    model = History
    form_class = HistoryForm
    template_name = "superadmin/history/history_create.html"
    success_url = reverse_lazy("history_view")
    extra_context = {
        "page_title": "History",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("history_view"),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["existing_images"] = self.object.history_image.all()
        return context

    def form_valid(self, form):
        self.objects = form.save()
        images = self.request.FILES.getlist("images")
        image_alt = self.request.POST.get("image_alt")

        for image in images:
            HistoryImage.objects.create(
                history=self.objects, image=image, image_alt=image_alt
            )
        self.object.history_image.update(image_alt=image_alt)

        messages.success(self.request, "History Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class HistoryImageDelete(LoginRequiredMixin, DeleteView):
    model = HistoryImage

    def get_success_url(self):
        return reverse_lazy("history_update", kwargs={"pk": self.object.history.pk})

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ContactListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = ContactUs
    context_object_name = "all_contacts"
    paginate_by = 10
    ordering = ["-id"]
    template_name = "superadmin/contact/contact_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Contact",
        "status": True,
    }


class EnquiryListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Enquiry
    context_object_name = "all_enquiry"
    paginate_by = 10
    template_name = "superadmin/enquiry/enquiry.html"
    search_field = "name"
    search_field = "created"
    extra_context = {
        "page_title": "Enquiry",
        "search_date": True,
        "status": True,
        "export": True,
    }


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
                        "phone_no": enquiry.mobile_no,
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
