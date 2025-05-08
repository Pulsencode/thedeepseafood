from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from company.models import (
    SEO,
    Blog,
    BlogImage,
    Brand,
    Certification,
    CompanyTestimonial,
    Event,
    EventImage,
    ManagementTeam,
    News,
    NewsImage,
    Promotion,
    PromotionImage,
    Supermarkets,
    History,
    HistoryImage
)


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = ("page_name", "meta_title", "meta_author", "status")
    list_filter = ("status", "page_name")
    search_fields = ("meta_title", "meta_description", "meta_keywords")
    list_editable = ("status",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "display_image", "sequence", "status")
    list_filter = ("status",)
    search_fields = ("name",)
    list_editable = ("sequence", "status")
    ordering = ("sequence",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "date", "sequence", "status")
    list_filter = ("status", "date")
    search_fields = ("title", "location", "description")
    list_editable = ("sequence", "status")
    ordering = ("-date",)


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ("event", "display_image", "status")
    list_filter = ("status", "event")
    search_fields = ("event__title", "image_alt")

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "location", "date", "sequence", "status")
    list_filter = ("status", "type", "date")
    search_fields = ("title", "content", "location")
    list_editable = ("sequence", "status")
    ordering = ("-date",)


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ("news", "display_image")
    list_filter = ("news",)
    search_fields = ("news__title", "image_alt")

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("title", "description", "location")
    list_editable = ("status",)


@admin.register(PromotionImage)
class PromotionImageAdmin(admin.ModelAdmin):
    list_display = ("promotion", "display_image")
    list_filter = ("promotion",)
    search_fields = ("promotion__title", "image_alt")

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("title", "content", "location")
    list_editable = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-date",)


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ("blog", "display_image")
    list_filter = ("blog",)
    search_fields = ("blog__title", "image_alt")

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(ManagementTeam)
class ManagementTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "display_image", "sequence", "status")
    list_filter = ("status",)
    search_fields = ("name", "role")
    list_editable = ("sequence", "status")
    ordering = ("sequence",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(CompanyTestimonial)
class CompanyTestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "display_image", "status")
    list_filter = ("status",)
    search_fields = ("name", "quote")
    list_editable = ("status",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("display_image", "sequence", "status")
    list_filter = ("status",)
    list_editable = ("sequence", "status")
    ordering = ("sequence",)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


@admin.register(Supermarkets)
class SupermarketsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("sequence", "__str__")
    ordering = ("sequence",)
    readonly_fields = ("sequence",)


admin.site.register(History)
admin.site.register(HistoryImage)
