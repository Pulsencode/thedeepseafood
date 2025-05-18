from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from company.models import Blog, News
from products.models import ProductDetails


class BlogSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(status=False)

    def lastmod(self, obj):
        return obj.published_date


class NewsSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return News.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.updated


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return ProductDetails.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, "updated_at") else None


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            "home",
            "about",
            "contact",
            "product",
            "career",
            "blog",
            "newsroom",
        ]

    def location(self, item):
        return reverse(item)
