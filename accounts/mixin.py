from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class SuperuserOrAdminRequiredMixin(UserPassesTestMixin):
    """Mixin to restrict access to superusers and users with 'admin' user_type."""

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.user_type == "admin"


class SuperAdminOrHrRequiredMixin(UserPassesTestMixin):
    """Mixin views to access both. user admin and hr"""

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return redirect("login_view")
        if user.is_superuser or user.user_type == "admin":
            return True
        if user.is_staff and user.user_type == "hr":
            return True
        return False
