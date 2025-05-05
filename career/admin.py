from django.contrib import admin
from .models import JobCategory, VacancyDetails, ApplicationDetails


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(VacancyDetails)
class VacancyDetailsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "salary")
    list_filter = ("category", "type")
    search_fields = ("title", "location")
    autocomplete_fields = ("category",)

    fieldsets = (
        (None, {"fields": ("title", "category", "location", "type", "salary", "hiring_status")}),
        ("Description", {"classes": ("collapse",), "fields": ("description",)}),
    )


@admin.register(ApplicationDetails)
class ApplicationDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "job",
        "notice_period",
        "vacancy",
    )
    list_filter = ("notice_period", "vacancy")
    search_fields = ("first_name", "last_name", "email", "job")
    autocomplete_fields = ("vacancy",)

    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "date_of_birth",
                ),
            },
        ),
        (
            "Job Info",
            {
                "fields": ("job", "vacancy", "start_date", "notice_period"),
            },
        ),
        (
            "Links & Attachments",
            {
                "fields": (
                    "linkedin_url",
                    "portfolio_url",
                    "upload_cv",
                    "cover_letter",
                ),
            },
        ),
        (
            "Additional Info",
            {
                "fields": ("message",),
            },
        ),
    )
