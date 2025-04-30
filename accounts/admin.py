from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("user_type", "phone_number", "address")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"fields": ("user_type", "phone_number", "address")}),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_type",
        "is_staff",
    )
    list_filter = ("user_type", "is_staff", "is_superuser")


admin.site.register(User, UserAdmin)
