import base64

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

# # import os
from django.core.files.base import ContentFile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from deepapp.helper import is_ajax, renderhelper
from company.models import Brand, Event
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


class CategoryCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/category/Category_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        # image = request.FILES.get('image')
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        brand_instance = request.POST.get("brand")
        brand = Brand.objects.get(id=brand_instance)

        category = Category(name=name, brand=brand, sequence=sequence)
        category.save()
        messages.success(request, "Category Added Successfully...!!")
        return redirect("category_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.filter(status=True).order_by("-id")
        return context


class CategoryUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/category/Category_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Category.objects.get(pk=id)
        brand = Brand.objects.all()
        return render(request, self.template_name, {"list": data, "brands": brand})

    def post(self, request, id):
        data = Category.objects.get(pk=id)
        # image = request.FILES.get('image')
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        brand_instance = request.POST.get("brand")
        brand = Brand.objects.get(id=brand_instance)

        # if image:
        # data.image = image
        data.name = name
        data.brand = brand
        data.sequence = sequence
        data.save()
        messages.success(request, "Category Updated Successfully...!!")
        return redirect("category_view")


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


class RecipeCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/recipe/recipe_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        image_alt = request.POST.get("image_alt")
        brand_instance = request.POST.get("brand")
        brand = Brand.objects.get(id=brand_instance)
        ingredient = request.POST.getlist("title[]")
        # amount = request.POST.getlist('amount[]')

        recipe = RecipeDetails(
            brand=brand, title=name, description=desc, image_alt=image_alt
        )
        recipe.save()

        for title in ingredient:
            if title:
                why = RecipeIngredients(recipe=recipe, title=title)
                why.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = RecipeImage(recipe=recipe, image=image)
            slider.save()

        messages.success(request, "Recipe Added Successfully...!!")
        return redirect("recipe_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = (
            Brand.objects.filter(status=True).exclude(name="Deep Sea").order_by("-id")
        )
        return context


class RecipeUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/recipe/recipe_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = RecipeDetails.objects.get(pk=id)
        brand = Brand.objects.exclude(name="Deep Sea")
        sliders = data.rec_image.all()
        why = data.rec_ind.all()
        return render(
            request,
            self.template_name,
            {"list": data, "brands": brand, "sliders": sliders, "whyc": why},
        )

    def post(self, request, id):
        data = get_object_or_404(RecipeDetails, pk=id)
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        image_alt = request.POST.get("image_alt")
        brand_instance = request.POST.get("brand")
        brand = Brand.objects.get(id=brand_instance)
        ingredient_titles = request.POST.getlist("title[]")
        # ingredient_amounts = request.POST.getlist("amount[]")

        # Update recipe details
        data.title = name
        data.brand = brand
        data.image_alt = image_alt
        data.description = desc
        data.save()

        # Handle existing and new ingredients
        existing_ingredients = RecipeIngredients.objects.filter(recipe=data)

        for title in ingredient_titles:
            if title:
                # Check if the pair already exists
                existing_record = existing_ingredients.filter(title=title).first()
                if existing_record:
                    # Update existing ingredient if found
                    existing_record.title = title
                    existing_record.save()
                else:
                    # Create a new ingredient if not found
                    new_ingredient = RecipeIngredients(recipe=data, title=title)
                    new_ingredient.save()

        # Delete existing ingredients that were removed in the update
        existing_ingredients.exclude(title__in=ingredient_titles).delete()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = RecipeImage(recipe=data, image=image)
            slider.save()

        messages.success(request, "Recipe Updated Successfully...!!")
        return redirect("recipe_view")


def delete_spec(request):
    if request.method == "GET":
        title = request.GET.get("why_heading")
        # amount = request.GET.get('why_description')

        try:
            # Delete from the WhyChooseHajj model
            RecipeIngredients.objects.filter(title=title).delete()

            return JsonResponse({"success": True})
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
    except Event.DoesNotExist:
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


class ProductCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        image = request.POST.get("brand-image")
        name = request.POST.get("name")
        brand = Brand.objects.get(name="Deep Sea")
        type = request.POST.get("type")
        sequence = request.POST.get("sequence")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")

        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        product = Product(
            name=name,
            brand=brand,
            type=type,
            title_tag=title_tag,
            metatag=metatag,
            keyword=keyword,
            canonical=canonical,
            sequence=sequence,
            image_alt=image_alt,
        )
        product.image.save(name + "." + ext, image_data, save=True)

        messages.success(request, "Product Added Successfully...!!")
        return redirect("product_view")


class ProductUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/deepsea-product/product_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Product.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Product.objects.get(pk=id)
        current_page = request.GET.get("page", None)
        image = request.POST.get("brand-image")
        brand = Brand.objects.get(name="Deep Sea")
        name = request.POST.get("name")
        type = request.POST.get("type")
        sequence = request.POST.get("sequence")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")

        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.image.save(name + "." + ext, image_data, save=True)
        data.name = name
        data.sequence = sequence
        data.brand = brand
        data.type = type
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        redirect_url = reverse("product_view")
        if current_page:
            redirect_url += f"?page={current_page}"

        messages.success(request, "Product Updated Successfully...!!")
        return redirect(redirect_url)


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
