from django.urls import path

from . import views

urlpatterns = [
    path("category-view", views.CategoryListView.as_view(), name="category_view"),
    path("category-add", views.CategoryCreateView.as_view(), name="category_add"),
    path(
        "category-update/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "subcategory-view", views.SubcategoryListView.as_view(), name="subcategory_view"
    ),
    path(
        "subcategory-add", views.SubcategoryCreateView.as_view(), name="subcategory_add"
    ),
    path(
        "subcategory-update/<int:id>/",
        views.SubcategoryUpdateView.as_view(),
        name="subcategory_update",
    ),
    path("product-view", views.ProductListView.as_view(), name="product_view"),
    path("product-add", views.ProductCreateView.as_view(), name="product_add"),
    path(
        "product-update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product-details-view",
        views.ProductDetailsListView.as_view(),
        name="product_details_view",
    ),
    path(
        "product-details-add",
        views.ProductDetailsCreateView.as_view(),
        name="product_details_add",
    ),
    path(
        "product-details-update/<int:pk>/",
        views.ProductDetailsUpdateView.as_view(),
        name="product_details_update",
    ),
]
