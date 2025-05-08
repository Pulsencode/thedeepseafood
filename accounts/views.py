from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


class ProfileView(TemplateView):
    template_name = "registration/password_confirm.html"


class LogoutView(TemplateView):
    template_name = "superadmin/login/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login_view")


class ChangePasswordView(TemplateView):
    template_name = "superadmin/profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Profile View"
        return context

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
            return redirect("password_change")

        return self.render_to_response(self.get_context_data())
