from django.urls import path
from . import views


urlpatterns = [
    path("", views.LoginView.as_view(), name="login_view"),
    path(
        "admin_dashboard/", views.AdminDashboardView.as_view(), name="admin_dashboard"
    ),
]
