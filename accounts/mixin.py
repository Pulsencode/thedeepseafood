from django.contrib.auth.mixins import UserPassesTestMixin


class SuperuserOrAdminRequiredMixin(UserPassesTestMixin):
    """Mixin to restrict access to superusers and users with 'admin' user_type."""

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.user_type == "admin"


class HROnlyAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.user_type == "hr"
