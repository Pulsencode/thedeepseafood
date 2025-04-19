from django.urls import path
from . import views


urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile_view"),
    path("change_password", views.ChangePasswordView.as_view(), name="change_password"),
    path("logout", views.LogoutView.as_view(), name="logout_view"),
]
