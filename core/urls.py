from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap,BlogSitemap,NewsSitemap




sitemaps = {
    "static": StaticViewSitemap,
    # "products": ProductSitemap,
    "blog": BlogSitemap,
    "news": NewsSitemap,
}





urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
    path("", include("public_interface.urls")),
    path("company/", include("company.urls")),
    path("career/", include("career.urls")),
    path("products/", include("products.urls")),
    path("accounts/", include("accounts.urls")),
    path("summernote/", include("django_summernote.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("administration/", include("administration.urls")),
]
