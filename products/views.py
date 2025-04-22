import base64

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

# import os
from django.core.files.base import ContentFile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView


from deepapp.helper import is_ajax, renderhelper
from company.models import Brand
from products.forms import CategoryForm, RecipeForm, RecipeIngredientFormSet, ProductForm
from products.models import (
    Category,
    Product,
    ProductDetails,
    RecipeDetails,
    RecipeImage,
    RecipeIngredients,
    Subcategory,
)


class CategoryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/category/Category_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Category"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Category.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Category.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Category.objects.get(id=item_id)
                except Category.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "category", "Category_view", context)


class CategoryCreateView(UserPassesTestMixin, CreateView):
    template_name = "superadmin/category/Category_create.html"
    form_class = CategoryForm

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Category Added Successfully...!!")
        return redirect("category_view")

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))


class CategoryUpdateView(UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "superadmin/category/Category_create.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('category_view')

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Category Updated Successfully...!!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class RecipeListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/recipe/recipe_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Recipe"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = RecipeDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(title__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                RecipeDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = RecipeDetails.objects.get(id=item_id)
                except RecipeDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "recipe", "recipe_view", context)


class RecipeCreateView(UserPassesTestMixin, CreateView):
    model = RecipeDetails
    form_class = RecipeForm
    template_name = "superadmin/recipe/recipe_create.html"
    success_url = reverse_lazy('recipe_view')

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = RecipeIngredientFormSet(self.request.POST)
        else:
            context['ingredient_formset'] = RecipeIngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']
        if ingredient_formset.is_valid():
            self.object = form.save()
            ingredient_formset.instance = self.object
            ingredient_formset.save()

            for image in self.request.FILES.getlist('files'):
                RecipeImage.objects.create(recipe=self.object, image=image)

            messages.success(self.request, "Recipe Added Successfully...!!")
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class RecipeUpdateView(UserPassesTestMixin, UpdateView):
    model = RecipeDetails
    form_class = RecipeForm
    template_name = "superadmin/recipe/recipe_create.html"
    success_url = reverse_lazy('recipe_view')
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = RecipeIngredientFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context['ingredient_formset'] = RecipeIngredientFormSet(instance=self.object)
        context['sliders'] = self.object.rec_image.all()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']
        if ingredient_formset.is_valid():
            self.object = form.save()
            ingredient_formset.instance = self.object
            ingredient_formset.save()

            for image in self.request.FILES.getlist('files'):
                RecipeImage.objects.create(recipe=self.object, image=image)

            messages.success(self.request, "Recipe Updated Successfully...!!")
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


def delete_spec(request):
    if request.method == "GET":
        ingredient_id = request.GET.get("id")
        try:
            ingredient = RecipeIngredients.objects.get(id=ingredient_id)
            ingredient.delete()
            return JsonResponse({"success": True})
        except RecipeIngredients.DoesNotExist:
            return JsonResponse({"success": False, "error": "Ingredient not found"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def delete_recipeslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = RecipeImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except RecipeImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


# deepsea product
class ProductListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product/product_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Product"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        homepage = request.GET.get("new")

        cd = Product.objects.filter(brand__name="Deep Sea").order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Product.objects.filter(id=item_id).update(status=status)
            if homepage:
                if homepage == "1":
                    homepage = True
                else:
                    homepage = False
                item_id = request.GET.get("item_id")
                Product.objects.filter(id=item_id).update(homepage=homepage)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Product.objects.get(id=item_id)
                except Product.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "deepsea-product", "product_view", context)


class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "superadmin/deepsea-product/product_create.html"
    success_url = reverse_lazy("product_view")

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def form_valid(self, form):
        image_data = self.request.POST.get("brand-image")
        if image_data:
            format, imgstr = image_data.split(";base64,")
            ext = format.split("/")[-1]
            img_file = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")
            form.instance.image.save(f"{form.cleaned_data['name']}.{ext}", img_file, save=False)
        messages.success(self.request, "Product Added Successfully...!!")
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "superadmin/deepsea-product/product_create.html"
    success_url = reverse_lazy("product_view")
    pk_url_kwarg = "id"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def form_valid(self, form):
        image_data = self.request.POST.get("brand-image")
        if image_data:
            format, imgstr = image_data.split(";base64,")
            ext = format.split("/")[-1]
            img_file = ContentFile(base64.b64decode(imgstr), name=f"temp.{ext}")
            form.instance.image.save(f"{form.cleaned_data['name']}.{ext}", img_file, save=False)
        messages.success(self.request, "Product Updated Successfully...!!")
        return super().form_valid(form)


# deepsea product details
class ProductDetailsListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product-details/product_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Product Details"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        # homepage = request.GET.get("new")

        cd = ProductDetails.objects.filter(product__brand__name="Deep Sea").order_by(
            "-id"
        )

        if is_ajax(request):
            if search:
                cd = cd.filter(product__name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                ProductDetails.objects.filter(id=item_id).update(status=status)
            # if homepage:
            #     if homepage == '1':
            #         homepage = True
            #     else:
            #         homepage = False
            #     item_id = request.GET.get("item_id")
            #     ProductDetails.objects.filter(id=item_id).update(homepage=homepage)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ProductDetails.objects.get(id=item_id)
                except ProductDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "deepsea-product-details", "product_view", context)


class ProductDetailsCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product-details/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("prod")
        product = Product.objects.get(id=product_id)
        category_id = request.POST.get("cat")
        category = Category.objects.get(id=category_id)
        sub = request.POST.get("sub")
        code = request.POST.get("code")
        weight = request.POST.get("weight")
        price = request.POST.get("price")
        origin = request.POST.get("origin")
        grade = request.POST.get("grade")
        packing = request.POST.get("packing")
        desc = request.POST.get("desc")
        ingredient = request.POST.get("ingredient")
        instruction = request.POST.get("instruction")
        storage = request.POST.get("storage")
        causion = request.POST.get("causion")

        product_details = ProductDetails(
            product=product,
            category=category,
            sub_categories=sub,
            price=price,
            product_code=code,
            net_weight=weight,
            origin=origin,
            grade=grade,
            packing=packing,
            description=desc,
            ingredients=ingredient,
            instructions=instruction,
            storage_instructions=storage,
            causion=causion,
        )
        product_details.save()

        messages.success(request, "Product Details Added Successfully...!!")
        return redirect("product_details_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(
            status=True, brand__name="Deep Sea"
        ).order_by("-id")
        context["category"] = Category.objects.filter(
            status=True, brand__name="Deep Sea"
        ).order_by("-id")
        return context


class ProductDetailsUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product-details/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = ProductDetails.objects.get(pk=id)
        category = Category.objects.filter(brand__name="Deep Sea").order_by("-id")
        products = Product.objects.filter(brand__name="Deep Sea").order_by("-id")

        return render(
            request,
            self.template_name,
            {"list": data, "products": products, "category": category},
        )

    def post(self, request, id):
        data = ProductDetails.objects.get(pk=id)
        current_page = request.GET.get("page", None)
        product_id = request.POST.get("prod")
        product = Product.objects.get(id=product_id)
        category_id = request.POST.get("cat")
        category = Category.objects.get(id=category_id)
        sub = request.POST.get("sub")
        code = request.POST.get("code")
        weight = request.POST.get("weight")
        price = request.POST.get("price")
        origin = request.POST.get("origin")
        grade = request.POST.get("grade")
        packing = request.POST.get("packing")
        desc = request.POST.get("desc")
        ingredient = request.POST.get("ingredient")
        instruction = request.POST.get("instruction")
        storage = request.POST.get("storage")
        causion = request.POST.get("causion")

        data.product = product
        data.category = category
        data.sub_categories = sub
        data.product_code = code
        data.grade = grade
        data.packing = packing
        data.desc = desc
        data.ingredients = ingredient
        data.instructions = instruction
        data.net_weight = weight
        data.causion = causion
        data.origin = origin
        data.price = price
        data.storage_instructions = storage
        data.save()

        redirect_url = reverse("product_details_view")
        if current_page:
            redirect_url += f"?page={current_page}"

        messages.success(request, " Product Details Updated Successfully...!!")
        return redirect(redirect_url)


# brand product
class BrandProductListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product/product_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Brand Product"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        # homepage = request.GET.get("new")

        cd = Product.objects.exclude(brand__name="Deep Sea").order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(
                    Q(name__icontains=search)
                    | Q(product_details__category__name__icontains=search)
                )
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Product.objects.filter(id=item_id).update(status=status)
            # if homepage:
            #     if homepage == '1':
            #         homepage = True
            #     else:
            #         homepage = False
            #     item_id = request.GET.get("item_id")
            #     Product.objects.filter(id=item_id).update(homepage=homepage)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Product.objects.get(id=item_id)
                except Product.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "brand-product", "product_view", context)


class BrandProductCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        image = request.POST.get("brand-image")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        brand_instance = request.POST.get("brand")
        image_alt = request.POST.get("image_alt")
        brand = Brand.objects.get(id=brand_instance)
        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        product = Product(
            name=name,
            brand=brand,
            title_tag=title_tag,
            metatag=metatag,
            keyword=keyword,
            canonical=canonical,
            sequence=sequence,
            image_alt=image_alt,
        )
        product.image.save(name + "." + ext, image_data, save=True)

        messages.success(request, "Product Added Successfully...!!")
        return redirect("brand_product_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.filter(status=True).order_by("-id")
        # context['sub'] = Subcategory.objects.filter(status=True).order_by('-id')
        return context


class BrandProductUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Product.objects.get(pk=id)
        brand = Brand.objects.filter(status=True)

        return render(request, self.template_name, {"list": data, "brands": brand})

    def post(self, request, id):
        data = Product.objects.get(pk=id)
        current_page = request.GET.get("page", None)
        image = request.POST.get("brand-image")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        brand_instance = request.POST.get("brand")
        image_alt = request.POST.get("image_alt")
        brand = Brand.objects.get(id=brand_instance)

        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.image.save(name + "." + ext, image_data, save=True)
        data.name = name
        data.brand = brand
        data.sequence = sequence
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        redirect_url = reverse("brand_product_view")
        if current_page:
            redirect_url += f"?page={current_page}"

        messages.success(request, "Product Updated Successfully...!!")
        return redirect(redirect_url)


class BrandProductDetailsListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product-details/product_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Brand Product Details"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        # homepage = request.GET.get("new")

        cd = ProductDetails.objects.exclude(product__brand__name="Deep Sea").order_by(
            "-id"
        )

        if is_ajax(request):
            if search:
                cd = cd.filter(product__name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                ProductDetails.objects.filter(id=item_id).update(status=status)
            # if homepage:
            #     if homepage == '1':
            #         homepage = True
            #     else:
            #         homepage = False
            #     item_id = request.GET.get("item_id")
            #     ProductDetails.objects.filter(id=item_id).update(homepage=homepage)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ProductDetails.objects.get(id=item_id)
                except ProductDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "brand-product-details", "product_view", context)


class BrandProductDetailsCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product-details/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product")
        product = Product.objects.get(id=product_id)
        category_id = request.POST.get("cat")
        category = Category.objects.get(id=category_id)
        weight = request.POST.get("weight")
        origin = request.POST.get("origin")
        storage = request.POST.get("storage")
        shelf = request.POST.get("shelf")
        cook = request.POST.get("cook")
        # Adding this with out the correct name so that the production code does not break
        ingredients = request.POST.get("ingredients")
        causion = request.POST.get(
            "causion"
        )  # This is now used for allergen information
        description = request.POST.get(
            "description"
        )  # This is now used for nutritional facts

        product_details = ProductDetails(
            product=product,
            category=category,
            net_weight=weight,
            origin=origin,
            storage_instructions=storage,
            shelf_life=shelf,
            how_to_cook=cook,
            ingredients=ingredients,
            causion=causion,
            description=description,
        )
        product_details.save()

        messages.success(request, "Brand Product Details Added Successfully...!!")
        return redirect("brand_product_details_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = (
            Product.objects.filter(status=True)
            .exclude(brand__name="Deep Sea")
            .order_by("-id")
        )
        return context


class BrandLoadCategory(View):
    template_name = "superadmin/brand-product-details/category_list.html"

    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            id = request.GET.get("id")
            # print('***brand id',id)

            try:
                product = Product.objects.get(id=id)
                brand = product.brand
                category = list(
                    Category.objects.filter(brand=brand).values("id", "name")
                )

                # print('***',category)
                context = {"category": category}
                template = loader.get_template(self.template_name)
                html_content = template.render(context, request)
                return JsonResponse({"status": True, "template": html_content})
            except Exception as e:
                print(str(e))
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


class BrandProductDetailsUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand-product-details/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = ProductDetails.objects.get(pk=id)
        brand = data.product.brand
        print(brand, "***brnd")
        category = Category.objects.filter(brand=brand).order_by("-id")
        products = Product.objects.exclude(brand__name="Deep Sea").order_by("-id")

        return render(
            request,
            self.template_name,
            {"list": data, "products": products, "category": category},
        )

    def post(self, request, id):
        data = ProductDetails.objects.get(pk=id)
        current_page = request.GET.get("page", None)
        product_id = request.POST.get("product")
        product = Product.objects.get(id=product_id)
        category_id = request.POST.get("cat")
        category = Category.objects.get(id=category_id)
        weight = request.POST.get("weight")
        origin = request.POST.get("origin")
        storage = request.POST.get("storage")
        shelf = request.POST.get("shelf")
        cook = request.POST.get("cook")
        ingredients = request.POST.get("ingredients")
        causion = request.POST.get(
            "causion"
        )  # This is now used for allergen information
        description = request.POST.get(
            "description"
        )  # This is now used for nutritional facts

        data.product = product
        data.category = category
        data.net_weight = weight
        data.shelf_life = shelf
        data.origin = origin
        data.storage_instructions = storage
        data.how_to_cook = cook
        data.ingredients = ingredients
        data.causion = causion
        data.description = description
        data.save()

        redirect_url = reverse("brand_product_details_view")
        if current_page:
            redirect_url += f"?page={current_page}"

        messages.success(request, " Brand Product Details Updated Successfully...!!")
        return redirect(redirect_url)


class SubcategoryListView(TemplateView):
    template_name = "superadmin/subcategory/Subcategory_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "subcategory"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Subcategory.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Subcategory.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Subcategory.objects.get(id=item_id)
                except Subcategory.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, 10)
            try:
                datas = paginator.get_page(page)
            except PageNotAnInteger:
                datas = paginator.get_page(1)
            except EmptyPage:
                datas = paginator.get_page(paginator.num_pages)
            context["datas"] = datas
            context["page"] = page
            template = loader.get_template(self.template_name)
            html_content = template.render(context, request)
            return JsonResponse({"status": True, "template": html_content})

        paginator = Paginator(cd, 10)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        return renderhelper(request, "subcategory", "Subcategory_view", context)


class SubcategoryCreateView(TemplateView):
    template_name = "superadmin/subcategory/Subcategory_create.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        sub = Subcategory(name=name)
        sub.save()
        messages.success(request, "Subcategory Added Successfully...!!")
        return redirect("subcategory_view")


class SubcategoryUpdateView(TemplateView):
    template_name = "superadmin/subcategory/Subcategory_create.html"

    def get(self, request, id):
        data = Subcategory.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Subcategory.objects.get(pk=id)
        name = request.POST.get("name")

        data.name = name
        data.save()

        messages.success(request, "Subcategory Updated Successfully...!!")
        return redirect("subcategory_view")
