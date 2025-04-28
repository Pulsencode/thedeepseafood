from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", include("public_interface.urls")),
    path("company/", include("company.urls")),
    path("career/", include("career.urls")),
    path("products/", include("products.urls")),
    path("accounts/", include("accounts.urls")),
    path("administration/", include("administration.urls")),
]
