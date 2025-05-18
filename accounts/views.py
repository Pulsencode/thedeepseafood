from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView


class LogoutView(TemplateView):
    template_name = "superadmin/login/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login_view")
