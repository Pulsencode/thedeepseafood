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
        "subcategory-update/<int:pk>/",
        views.SubcategoryUpdateView.as_view(),
        name="subcategory_update",
    ),
    # path("recipe-view", views.RecipeListView.as_view(), name="recipe_view"),
    # path("recipe-add", views.RecipeCreateView.as_view(), name="recipe_add"),
    # path(
    #     "recipe-update/<int:pk>/",
    #     views.RecipeUpdateView.as_view(),
    #     name="recipe_update",
    # ),
    # #
    # path("delete-ingredient/", views.delete_spec, name="delete_ingredient"),
    # path(
    #     "delete-recipeslider/<int:image_id>/",
    #     views.delete_recipeslider,
    #     name="delete_recipeslider",
    # ),
    #
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
    # brandproduct
    path(
        "brand-product-view",
        views.BrandProductListView.as_view(),
        name="brand_product_view",
    ),
    path(
        "brand-product-add",
        views.BrandProductCreateView.as_view(),
        name="brand_product_add",
    ),
    path(
        "brand-product-update/<int:pk>/",
        views.BrandProductUpdateView.as_view(),
        name="brand_product_update",
    ),
    path(
        "brand-product-details-view",
        views.BrandProductDetailsListView.as_view(),
        name="brand_product_details_view",
    ),
    path(
        "brandproduct-getcategory/",
        views.BrandLoadCategory.as_view(),
        name="getbrandcategory",
    ),
    path(
        "brand-product-details-add",
        views.BrandProductDetailsCreateView.as_view(),
        name="brand_product_details_add",
    ),
    path(
        "brand-product-details-update/<int:pk>/",
        views.BrandProductDetailsUpdateView.as_view(),
        name="brand_product_details_update",
    ),
]
