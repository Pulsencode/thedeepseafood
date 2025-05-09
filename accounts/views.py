from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout


class LogoutView(TemplateView):
    template_name = "superadmin/login/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login_view")
