from django.contrib import admin

from .models import Category, Product, ProductDetails, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "sequence", "created")
    list_filter = ("brand",)
    search_fields = ("name",)
    ordering = ("sequence",)
    prepopulated_fields = {"name": ("name",)}


class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "homepage", "created")
    list_filter = ("type", "homepage")
    search_fields = ("name",)
    ordering = ("sequence",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductDetailsInline]


class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ("product", "category", "price", "origin")
    list_filter = ("category",)
    search_fields = ("product__name", "product_code", "origin")


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name__name",)


# Registering all
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
