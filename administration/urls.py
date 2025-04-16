from django.urls import path
from administration import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login_view"),
]
