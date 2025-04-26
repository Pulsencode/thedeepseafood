from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile_view"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="superadmin/profile/profile.html"
        ),
        name="password_change",
    ),
    path(
        "change-password/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("logout", views.LogoutView.as_view(), name="logout_view"),
]
