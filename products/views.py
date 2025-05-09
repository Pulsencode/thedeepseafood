# import base64

from django.contrib import messages

# # import os
# from django.core.files.base import ContentFile
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from django.db.models import Q
# from django.http import JsonResponse
from django.shortcuts import redirect, render

# from django.template import loader
from django.urls import reverse_lazy

# from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, ListView

# from company.models import Brand
from products.forms import (
    # BrandProductDetailsForm,
    # BrandProductForm,
    CategoryForm,
    ProductDetailsForm,
    ProductForm,
)
from products.models import Category, Product, ProductDetails, Subcategory

# from public_interface.utils import is_ajax, render_helper
from company.mixin import SearchAndStatusFilterMixin, StatusUpdateAndDeleteMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import SuperuserOrAdminRequiredMixin


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


# class RecipeListView(AdminPermissionMixin, TemplateView):
#     template_name = "superadmin/recipe/recipe_list.html"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Recipe"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")

#         # cd = RecipeDetails.objects.all().order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(title__icontains=search)
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 # RecipeDetails.objects.filter(id=item_id).update(status=status)
#             if delete:
#                 item_id = request.GET.get("item_id")
#                 # try:
#                 #     datas = RecipeDetails.objects.get(id=item_id)
#                 # except RecipeDetails.DoesNotExist:
#                 #     datas = None
#                 if datas:
#                     datas.delete()
#             paginator = Paginator(cd, 10)
#             try:
#                 datas = paginator.get_page(page)
#             except PageNotAnInteger:
#                 datas = paginator.get_page(1)
#             except EmptyPage:
#                 datas = paginator.get_page(paginator.num_pages)
#             context["datas"] = datas
#             context["page"] = page
#             template = loader.get_template(self.template_name)
#             html_content = template.render(context, request)
#             return JsonResponse({"status": True, "template": html_content})

#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         context["path"] = path

#         return render_helper(request, "recipe", "recipe_view", context)


# class RecipeCreateView(AdminPermissionMixin, CreateView):
#     model = RecipeDetails
#     form_class = RecipeForm
#     template_name = "superadmin/recipe/recipe_create.html"
#     success_url = reverse_lazy("recipe_view")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context["ingredient_formset"] = RecipeIngredientFormSet(self.request.POST)
#         else:
#             context["ingredient_formset"] = RecipeIngredientFormSet()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         ingredient_formset = context["ingredient_formset"]
#         if ingredient_formset.is_valid():
#             self.object = form.save()
#             ingredient_formset.instance = self.object
#             ingredient_formset.save()

#             for image in self.request.FILES.getlist("files"):
#                 RecipeImage.objects.create(recipe=self.object, image=image)

#             messages.success(self.request, "Recipe Added Successfully...!!")
#             return super().form_valid(form)
#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(self.request, errors)
#             return self.form_invalid(form)


# class RecipeUpdateView(AdminPermissionMixin, UpdateView):
#     model = RecipeDetails
#     form_class = RecipeForm
#     template_name = "superadmin/recipe/recipe_create.html"
#     success_url = reverse_lazy("recipe_view")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context["ingredient_formset"] = RecipeIngredientFormSet(
#                 self.request.POST, instance=self.object
#             )
#         else:
#             context["ingredient_formset"] = RecipeIngredientFormSet(
#                 instance=self.object
#             )
#         context["sliders"] = self.object.ingredients.all()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         ingredient_formset = context["ingredient_formset"]
#         if ingredient_formset.is_valid():
#             self.object = form.save()
#             ingredient_formset.instance = self.object
#             ingredient_formset.save()

#             for image in self.request.FILES.getlist("files"):
#                 RecipeImage.objects.create(recipe=self.object, image=image)

#             messages.success(self.request, "Recipe Updated Successfully...!!")
#             return super().form_valid(form)
#         else:
#             return self.form_invalid(form)


# def delete_spec(request):
#     if request.method == "GET":
#         ingredient_id = request.GET.get("id")
#         try:
#             ingredient = RecipeIngredients.objects.get(id=ingredient_id)
#             ingredient.delete()
#             return JsonResponse({"success": True})
#         except RecipeIngredients.DoesNotExist:
#             return JsonResponse({"success": False, "error": "Ingredient not found"})
#         except Exception as e:
#             return JsonResponse({"success": False, "error": str(e)})

#     return JsonResponse({"success": False, "error": "Invalid request method"})


# def delete_recipeslider(request, image_id):
#     try:
#         # Get the image by its ID and delete it
#         image = RecipeImage.objects.get(pk=image_id)
#         image.image.delete()  # Delete the image file
#         image.delete()  # Delete the database record
#         return JsonResponse({"success": True})
#     except RecipeImage.DoesNotExist:
#         return JsonResponse({"success": False, "error": "Image not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)}, status=500)


# deepsea product
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


# brand product
# class BrandProductListView(TemplateView):
#     template_name = "superadmin/brand-product/product_list.html"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Brand Product"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")
#         # homepage = request.GET.get("new")

#         cd = Product.objects.exclude(brand__name="Deep Sea").order_by("-id")

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(
#                     Q(name__icontains=search)
#                     | Q(product_details__category__name__icontains=search)
#                 )
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 Product.objects.filter(id=item_id).update(status=status)

#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = Product.objects.get(id=item_id)
#                 except Product.DoesNotExist:
#                     datas = None
#                 if datas:
#                     datas.delete()

#             paginator = Paginator(cd, 10)
#             try:
#                 datas = paginator.get_page(page)
#             except PageNotAnInteger:
#                 datas = paginator.get_page(1)
#             except EmptyPage:
#                 datas = paginator.get_page(paginator.num_pages)
#             context["datas"] = datas
#             context["page"] = page
#             template = loader.get_template(self.template_name)
#             html_content = template.render(context, request)
#             return JsonResponse({"status": True, "template": html_content})

#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         context["path"] = path

#         return render_helper(request, "brand-product", "product_view", context)


# class BrandProductCreateView(AdminPermissionMixin, CreateView):
#     model = Brand
#     form_class = BrandProductForm
#     template_name = "superadmin/brand-product/product_create.html"
#     success_url = reverse_lazy("brand_product_view")

#     def form_valid(self, form):
#         image_data = self.request.POST.get("brand-image")
#         if not image_data:
#             form.add_error(None, "Image is required.")
#             return self.form_invalid(form)

#         try:
#             format, imgstr = image_data.split(";base64,")
#             ext = format.split("/")[-1]
#             decoded_image = base64.b64decode(imgstr)
#             file_name = f"{form.cleaned_data['name']}.{ext}"

#             form.instance.image.save(file_name, ContentFile(decoded_image), save=False)
#         except Exception as e:
#             form.add_error(None, f"Invalid image data: {str(e)}")
#             return self.form_invalid(form)

#         messages.success(self.request, "Product Added Successfully...!!")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         for error_list in form.errors.values():
#             for errors in error_list:
#                 messages.error(self.request, errors)
#         return super().form_invalid(form)


# class BrandProductUpdateView(AdminPermissionMixin, UpdateView):
#     model = Product
#     form_class = BrandProductForm
#     template_name = "superadmin/brand-product/product_create.html"
#     success_url = reverse_lazy("brand_product_view")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["brands"] = Brand.objects.filter(status=True).order_by("-id")
#         return context

#     def form_valid(self, form):
#         image_data = self.request.POST.get("brand-image")
#         if image_data:
#             format, imgstr = image_data.split(";base64,")
#             ext = format.split("/")[-1]
#             decoded_image = base64.b64decode(imgstr)
#             form.instance.image.save(
#                 form.cleaned_data["name"] + "." + ext,
#                 ContentFile(decoded_image),
#                 save=False,
#             )

#         messages.success(self.request, "Product Updated Successfully...!!")
#         return super().form_valid(form)


# class BrandProductDetailsListView(TemplateView):
#     template_name = "superadmin/brand-product-details/product_list.html"

#     def get(self, request, *args, **kwargs):
#         context = {}
#         path = "Brand Product Details"
#         page = request.GET.get("page", 1)

#         search = request.GET.get("search")
#         delete = request.GET.get("delete")
#         status = request.GET.get("status")
#         sts = request.GET.get("sts")
#         # homepage = request.GET.get("new")

#         cd = ProductDetails.objects.exclude(product__brand__name="Deep Sea").order_by(
#             "-id"
#         )

#         if is_ajax(request):
#             if search:
#                 cd = cd.filter(product__name__icontains=search)
#             if sts:
#                 cd = cd.filter(status=sts)
#             if status:
#                 if status == "1":
#                     status = True
#                 else:
#                     status = False
#                 item_id = request.GET.get("item_id")
#                 ProductDetails.objects.filter(id=item_id).update(status=status)

#             if delete:
#                 item_id = request.GET.get("item_id")
#                 try:
#                     datas = ProductDetails.objects.get(id=item_id)
#                 except ProductDetails.DoesNotExist:
#                     datas = None
#                 if datas:
#                     datas.delete()

#             paginator = Paginator(cd, 10)
#             try:
#                 datas = paginator.get_page(page)
#             except PageNotAnInteger:
#                 datas = paginator.get_page(1)
#             except EmptyPage:
#                 datas = paginator.get_page(paginator.num_pages)
#             context["datas"] = datas
#             context["page"] = page
#             template = loader.get_template(self.template_name)
#             html_content = template.render(context, request)
#             return JsonResponse({"status": True, "template": html_content})

#         paginator = Paginator(cd, 10)
#         try:
#             datas = paginator.get_page(page)
#         except PageNotAnInteger:
#             datas = paginator.get_page(1)
#         except EmptyPage:
#             datas = paginator.get_page(paginator.num_pages)
#         context["datas"] = datas
#         context["page"] = page
#         context["path"] = path

#         return render_helper(request, "brand-product-details", "product_view", context)


# class BrandProductDetailsCreateView(AdminPermissionMixin, CreateView):
#     model = ProductDetails
#     form_class = BrandProductDetailsForm
#     template_name = "superadmin/brand-product-details/product_create.html"
#     success_url = reverse_lazy("brand_product_details_view")

#     def form_valid(self, form):
#         messages.success(self.request, "Brand Product Details Added Successfully...!!")
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = (
#             Product.objects.filter(status=True)
#             .exclude(brand__name="Deep Sea")
#             .order_by("-id")
#         )
#         return context


# class BrandProductDetailsUpdateView(AdminPermissionMixin, UpdateView):
#     model = ProductDetails
#     form_class = BrandProductDetailsForm
#     template_name = "superadmin/brand-product-details/product_create.html"
#     success_url = reverse_lazy("brand_product_details_view")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         data = self.get_object()
#         context["products"] = Product.objects.exclude(brand__name="Deep Sea").order_by(
#             "-id"
#         )
#         context["category"] = Category.objects.filter(
#             brand=data.product.brand
#         ).order_by("-id")
#         return context

#     def form_valid(self, form):
#         messages.success(
#             self.request, "Brand Product Details Updated Successfully...!!"
#         )
#         return super().form_valid(form)


# class BrandLoadCategory(View):
#     template_name = "superadmin/brand-product-details/category_list.html"

#     def get(self, request):
#         if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
#             id = request.GET.get("id")

#             try:
#                 product = Product.objects.get(id=id)
#                 brand = product.brand
#                 category = list(
#                     Category.objects.filter(brand=brand).values("id", "name")
#                 )

#                 context = {"category": category}
#                 template = loader.get_template(self.template_name)
#                 html_content = template.render(context, request)
#                 return JsonResponse({"status": True, "template": html_content})
#             except Exception as e:
#                 print(str(e))
#                 return JsonResponse({"error": str(e)}, status=500)

#         return JsonResponse({"error": "Invalid request"}, status=400)
