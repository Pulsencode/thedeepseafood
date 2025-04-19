from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages


# Create your views here.
class LoginView(TemplateView):
    template_name = "superadmin/login/login.html"

    def post(self, request, *args, **kwargs):
        uname = self.request.POST.get("uname")
        password = self.request.POST.get("pass")
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect("index_view")
            else:
                messages.error(request, "You are not a verified user")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login_view")


class ProfileView(TemplateView):
    template_name = "superadmin/profile/profile.html"


class ChangePasswordView(TemplateView):
    template_name = "superadmin/profile/profile.html"

    def post(self, request, *args, **kwargs):
        old_password = self.request.POST.get("old_password")
        new_password1 = self.request.POST.get("new_password1")
        new_password2 = self.request.POST.get("new_password2")

        if not request.user.check_password(old_password):
            messages.error(request, "Invalid old password.")
        elif new_password1 != new_password2:
            messages.error(request, "New passwords do not match.")
        else:
            user = request.user
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(
                request, user
            )  # Update session with new password hash
            messages.success(request, "Your password has been changed successfully.")
            return redirect("change_password")


class LogoutView(TemplateView):
    template_name = "superadmin/login/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login_view")
