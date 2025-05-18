from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from accounts.mixin import SuperuserOrAdminRequiredMixin
from company.mixin import SearchAndStatusFilterMixin, StatusUpdateAndDeleteMixin
from products.forms import CategoryForm, ProductDetailsForm, ProductForm
from products.models import Category, Product, ProductDetails, Subcategory


class CategoryListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Category
    paginate_by = 10
    context_object_name = "all_category"
    template_name = "superadmin/category/Category_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Category",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("category_add"),
    }


class CategoryCreateView(LoginRequiredMixin, SuperuserOrAdminRequiredMixin, CreateView):
    model = Category
    template_name = "superadmin/category/Category_create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_view")
    extra_context = {
        "page_title": "Create Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("category_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Category Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CategoryUpdateView(LoginRequiredMixin, SuperuserOrAdminRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "superadmin/category/Category_create.html"
    success_url = reverse_lazy("category_view")
    extra_context = {
        "page_title": "Update Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("category_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Category Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class SubcategoryListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Subcategory
    paginate_by = 10
    ordering = ["-id"]
    context_object_name = "all_subcategory"
    template_name = "superadmin/subcategory/Subcategory_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Sub Category",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("subcategory_add"),
    }


class SubcategoryCreateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, TemplateView
):
    template_name = "superadmin/subcategory/Subcategory_create.html"

    extra_context = {
        "page_title": "Sub Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("subcategory_view"),
    }

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        sub = Subcategory(name=name)
        sub.save()
        messages.success(request, "Subcategory Added Successfully...!!")
        return redirect("subcategory_view")


class SubcategoryUpdateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, TemplateView
):
    template_name = "superadmin/subcategory/Subcategory_create.html"
    extra_context = {
        "page_title": "Sub Category",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("subcategory_view"),
    }

    def get(self, request, id):
        data = Subcategory.objects.get(pk=id)
        return render(request, self.template_name, {"subcategory": data})

    def post(self, request, id):
        data = Subcategory.objects.get(pk=id)
        name = request.POST.get("name")

        data.name = name
        data.save()

        messages.success(request, "Subcategory Updated Successfully...!!")
        return redirect("subcategory_view")


class ProductListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = Product
    context_object_name = "all_products"
    paginate_by = 10
    template_name = "superadmin/deepsea-product/product_view.html"
    search_field = "name"
    extra_context = {
        "page_title": "Product",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("product_add"),
    }


class ProductCreateView(LoginRequiredMixin, SuperuserOrAdminRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "superadmin/deepsea-product/product_create.html"
    success_url = reverse_lazy("product_view")
    extra_context = {
        "page_title": "Product",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("product_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Product Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, SuperuserOrAdminRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "superadmin/deepsea-product/product_create.html"
    success_url = reverse_lazy("product_view")
    extra_context = {
        "page_title": "Product",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("product_view"),
    }

    def form_valid(self, form):

        # image_data = self.request.POST.get("brand-image")
        # if image_data:
        #     format, imgstr = image_data.split(";base64,")
        #     ext = format.split("/")[-1]
        #     img_file = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")
        #     form.instance.image.save(
        #         f"{form.cleaned_data['name']}.{ext}", img_file, save=False
        #     )
        messages.success(self.request, "Product Added Successfully...!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# deepsea product details
class ProductDetailsListView(
    LoginRequiredMixin,
    SuperuserOrAdminRequiredMixin,
    SearchAndStatusFilterMixin,
    StatusUpdateAndDeleteMixin,
    ListView,
):
    model = ProductDetails
    context_object_name = "products_details"
    paginate_by = 10
    search_field = "product__name"
    template_name = "superadmin/deepsea-product-details/product_view.html"
    extra_context = {
        "page_title": "Product Details",
        "path_name": "Add New",
        "add_item": True,
        "path_url": reverse_lazy("product_details_add"),
    }


class ProductDetailsCreateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, CreateView
):
    model = ProductDetails
    form_class = ProductDetailsForm
    template_name = "superadmin/deepsea-product-details/product_create.html"
    success_url = reverse_lazy("product_details_view")
    extra_context = {
        "page_title": "Deep Sea Product Details",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("product_details_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Product Details Added Successfully…!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class ProductDetailsUpdateView(
    LoginRequiredMixin, SuperuserOrAdminRequiredMixin, UpdateView
):
    model = ProductDetails
    form_class = ProductDetailsForm
    template_name = "superadmin/deepsea-product-details/product_create.html"
    success_url = reverse_lazy("product_details_view")
    extra_context = {
        "page_title": "Deep Sea Product Details",
        "path_name": "View All",
        "view_item": True,
        "path_url": reverse_lazy("product_details_view"),
    }

    def form_valid(self, form):
        messages.success(self.request, "Product Details Updated Successfully…!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)
