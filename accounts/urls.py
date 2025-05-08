from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile_view"),
    path(
        "change-password/",
        views.ChangePasswordView.as_view(), name="password_change",
    ),
    path("logout", views.LogoutView.as_view(), name="logout_view"),
]
