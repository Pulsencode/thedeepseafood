from django.urls import path
from . import views


urlpatterns = [
    path("login", views.LoginView.as_view(), name="login_view"),
    path("index", views.IndexView.as_view(), name="index_view"),
]
