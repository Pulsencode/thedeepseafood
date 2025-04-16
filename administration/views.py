import base64
from datetime import datetime

# from deepapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "administration/login.html"

    def post(self, request, *args, **kwargs):
        uname = self.request.POST.get("uname")
        password = self.request.POST.get("pass")
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect("index_view")
            else:
                messages.error(request, "You are not a verified user")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login_view")


class LogoutView(TemplateView):
    template_name = "administration/login.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login_view")


class ProfileView(TemplateView):
    template_name = "superadmin/profile/profile.html"


class ChangePasswordView(TemplateView):
    template_name = "superadmin/profile/profile.html"

    def post(self, request, *args, **kwargs):
        old_password = self.request.POST.get("old_password")
        new_password1 = self.request.POST.get("new_password1")
        new_password2 = self.request.POST.get("new_password2")

        if not request.user.check_password(old_password):
            messages.error(request, "Invalid old password.")
        elif new_password1 != new_password2:
            messages.error(request, "New passwords do not match.")
        else:
            user = request.user
            user.set_password(new_password1)
            user.save()
            update_session_auth_hash(
                request, user
            )  # Update session with new password hash
            messages.success(request, "Your password has been changed successfully.")
            return redirect("change_password")


# index
class IndexView(TemplateView):
    template_name = "superadmin/index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = Brand.objects.filter(status=True).order_by("-id").count()
        category = Category.objects.filter(status=True).order_by("-id").count()
        job = JobCategory.objects.filter(status=True).order_by("-id").count()
        recipe = RecipeDetails.objects.filter(status=True).order_by("-id").count()
        gallery = EventGallery.objects.filter(status=True).order_by("-id").count()
        news = NewsDetails.objects.filter(status=True).order_by("-id").count()
        promo = PromotionDetails.objects.filter(status=True).order_by("-id").count()
        blog = BlogDetails.objects.filter(status=True).order_by("-id").count()
        team = ManagementTeam.objects.filter(status=True).order_by("-id").count()
        testi = CompanyTestimonial.objects.filter(status=True).order_by("-id").count()
        career = VaccancyDetails.objects.filter(status=True).order_by("-id").count()
        appli = ApplicationDetails.objects.filter(status=True).order_by("-id").count()
        history = HistoryDetails.objects.filter(status=True).order_by("-id").count()
        contact = ContactUsDetails.objects.filter().order_by("-id").count()
        enquiry = EnquiryDetails.objects.filter().order_by("-id").count()
        product = Product.objects.filter().order_by("-id").count()
        context["product"] = product
        context["enquiry"] = enquiry
        context["contact"] = contact
        context["history"] = history
        context["appli"] = appli
        context["career"] = career
        context["testi"] = testi
        context["team"] = team
        context["blog"] = blog
        context["promo"] = promo
        context["news"] = news
        context["gallery"] = gallery
        context["recipe"] = recipe
        context["job"] = job
        context["category"] = category
        context["brand"] = brand
        return context


# Brand
class BrandListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand/brand_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Brand"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Brand.objects.exclude(name="Deep Sea").order_by("-id")

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
                Brand.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Brand.objects.get(id=item_id)
                except Brand.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        # print(cd)
        return renderhelper(request, "brand", "brand_view", context)


class BrandCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand/brand_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        image = request.POST.get("brand-image")
        name = request.POST.get("name")
        image_alt = request.POST.get("image_alt")
        sequence = request.POST.get("sequence")

        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        brand = Brand(name=name, image_alt=image_alt, sequence=sequence)
        brand.logo.save(name + "." + ext, image_data, save=True)
        messages.success(request, "Brand Added Successfully...!!")
        return redirect("brand_view")


class BrandUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/brand/brand_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Brand.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Brand.objects.get(pk=id)
        image = request.POST.get("brand-image")
        name = request.POST.get("name")
        image_alt = request.POST.get("image_alt")
        sequence = request.POST.get("sequence")

        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.logo.save(name + "." + ext, image_data, save=True)
        data.name = name
        data.image_alt = image_alt
        data.sequence = sequence
        data.save()
        messages.success(request, "Brand Updated Successfully...!!")
        return redirect("brand_view")


# Category
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
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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


# jobCategory
class JobCategoryListView(TemplateView):
    template_name = "superadmin/job category/job_category_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "JobCategory"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = JobCategory.objects.all().order_by("-id")

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
                JobCategory.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = JobCategory.objects.get(id=item_id)
                except JobCategory.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "job category", "job_category_view", context)


class JobCategoryCreateView(TemplateView):
    template_name = "superadmin/job category/job_category_create.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        jcategory = JobCategory(name=name)
        jcategory.save()
        messages.success(request, "Job category Added Successfully...!!")
        return redirect("job_category_view")


class JobCategoryUpdateView(TemplateView):
    template_name = "superadmin/job category/job_category_create.html"

    def get(self, request, id):
        data = JobCategory.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = JobCategory.objects.get(pk=id)
        name = request.POST.get("name")

        data.name = name
        data.save()
        messages.success(request, "Job Category Updated Successfully...!!")
        return redirect("job_category_view")


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
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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
        ingredient_amounts = request.POST.getlist("amount[]")

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
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


# Gallery
class GalleryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Event Gallery"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = EventGallery.objects.all().order_by("-id")

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
                EventGallery.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = EventGallery.objects.get(id=item_id)
                except EventGallery.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "event gallery", "event_gallery_view", context)


class GalleryCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        # name = request.POST.get('name')
        location = request.POST.get("location")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        gallery = EventGallery(
            title=title,
            location=location,
            description=desc,
            date=date,
            sequence=sequence,
            image_alt=image_alt,
        )
        gallery.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = EventGalleryImage(event=gallery, image=image)
            slider.save()
        messages.success(request, "Gallery Added Successfully...!!")
        return redirect("gallery_view")


class GalleryUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/event gallery/event_gallery_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = EventGallery.objects.get(pk=id)
        sliders = data.gallery_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = EventGallery.objects.get(pk=id)
        sliders = data.gallery_image.all()
        title = request.POST.get("title")
        # name = request.POST.get('name')
        location = request.POST.get("location")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        # data.name = name
        data.location = location
        data.sequence = sequence
        data.description = desc
        data.image_alt = image_alt
        data.date = date
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = EventGalleryImage(event=data, image=image)
            slider.save()
        messages.success(request, "Gallery Updated Successfully...!!")
        return redirect("gallery_view")


def delete_slider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = EventGalleryImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class NewsListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "News"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = NewsDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                NewsDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = NewsDetails.objects.get(id=item_id)
                except NewsDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "news", "news_view", context)


class NewsCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        type = request.POST.get("type")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        news = NewsDetails(
            sequence=sequence,
            title=title,
            name=name,
            location=location,
            description=desc,
            date=date,
            type=type,
            image_alt=image_alt,
            title_tag=title_tag,
            metatag=metatag,
            keyword=keyword,
            canonical=canonical,
        )
        news.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = NewsGalleryImage(news=news, image=image)
            slider.save()
        messages.success(request, "News Added Successfully...!!")
        return redirect("news_view")


class NewsUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/news/news_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = NewsDetails.objects.get(pk=id)
        sliders = data.news_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = NewsDetails.objects.get(pk=id)
        sliders = data.news_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        type = request.POST.get("type")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.sequence = sequence
        data.type = type
        data.location = location
        data.description = desc
        data.date = date
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = NewsGalleryImage(news=data, image=image)
            slider.save()
        messages.success(request, "News Updated Successfully...!!")
        return redirect("news_view")


def delete_newsslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = NewsGalleryImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class PromotionListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Promotion"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = PromotionDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                PromotionDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = PromotionDetails.objects.get(id=item_id)
                except PromotionDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "promotion", "promotion_info_view", context)


class PromotionCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        promotion = PromotionDetails(
            title=title, name=name, location=location, description=desc, date=date
        )
        promotion.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = PromotionImage(promotion=promotion, image=image)
            slider.save()
        messages.success(request, "Promotion Added Successfully...!!")
        return redirect("promotion_view")


class PromotionUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/promotion/promotion_info_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = PromotionDetails.objects.get(pk=id)
        sliders = data.promo_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = PromotionDetails.objects.get(pk=id)
        sliders = data.promo_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.location = location
        data.description = desc
        data.date = date
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = PromotionImage(promotion=data, image=image)
            slider.save()
        messages.success(request, "Promotion Updated Successfully...!!")
        return redirect("promotion_view")


def delete_promotionslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = PromotionImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class BlogListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/blog/Blog_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Blog"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = BlogDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(Q(name__icontains=search) | Q(title__icontains=search))
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                BlogDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = BlogDetails.objects.get(id=item_id)
                except BlogDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "blog", "Blog_view", context)


class BlogCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/blog/Blog_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        blog = BlogDetails(
            title=title,
            name=name,
            location=location,
            description=desc,
            date=date,
            title_tag=title_tag,
            metatag=metatag,
            keyword=keyword,
            canonical=canonical,
            image_alt=image_alt,
        )
        blog.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = BlogImage(blog=blog, image=image)
            slider.save()
        messages.success(request, "Blog Added Successfully...!!")
        return redirect("blog_view")


class BlogUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/blog/Blog_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = BlogDetails.objects.get(pk=id)
        sliders = data.blog_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = BlogDetails.objects.get(pk=id)
        sliders = data.blog_image.all()
        title = request.POST.get("title")
        name = request.POST.get("name")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")
        image_alt = request.POST.get("image_alt")
        date_str = request.POST.get("date")
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = None

        data.title = title
        data.name = name
        data.location = location
        data.description = desc
        data.date = date
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.image_alt = image_alt
        data.save()

        # Update Slider images for the Country
        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = BlogImage(blog=data, image=image)
            slider.save()
        messages.success(request, "Blog Updated Successfully...!!")
        return redirect("blog_view")


def delete_blogslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = BlogImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class TeamListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/team/management_team_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Team"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = ManagementTeam.objects.all().order_by("-id")

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
                ManagementTeam.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ManagementTeam.objects.get(id=item_id)
                except ManagementTeam.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "team", "management_team_view", context)


class TeamCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/team/management_team_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        designation = request.POST.get("desig")
        name = request.POST.get("name")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        image = request.POST.get("team-image")
        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        team = ManagementTeam(
            name=name, sequence=sequence, designation=designation, image_alt=image_alt
        )
        team.image.save(name + "." + ext, image_data, save=True)
        team.save()

        messages.success(request, "Team Added Successfully...!!")
        return redirect("team_view")


class TeamUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/team/management_team_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = ManagementTeam.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = ManagementTeam.objects.get(pk=id)
        designation = request.POST.get("desig")
        sequence = request.POST.get("sequence")
        image_alt = request.POST.get("image_alt")
        name = request.POST.get("name")
        image = request.POST.get("team-image")

        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.image = image_data
        data.name = name
        data.sequence = sequence
        data.designation = designation
        data.image_alt = image_alt
        data.save()

        messages.success(request, "Team Updated Successfully...!!")
        return redirect("team_view")


class TestimonialListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/testimonial/testimonial_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Testimonial"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = CompanyTestimonial.objects.all().order_by("-id")

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
                CompanyTestimonial.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = CompanyTestimonial.objects.get(id=item_id)
                except CompanyTestimonial.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "testimonial", "testimonial_view", context)


class TestimonialCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/testimonial/testimonial_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        desc = request.POST.get("desc")
        name = request.POST.get("name")
        image_alt = request.POST.get("image_alt")
        image = request.POST.get("testi-image")
        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        testi = CompanyTestimonial(name=name, message=desc, image_alt=image_alt)
        testi.image.save(name + "." + ext, image_data, save=True)
        testi.save()

        messages.success(request, "Testimonial Added Successfully...!!")
        return redirect("testimonial_view")


class TestimonialUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/testimonial/testimonial_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = CompanyTestimonial.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = CompanyTestimonial.objects.get(pk=id)
        desc = request.POST.get("desc")
        name = request.POST.get("name")
        image_alt = request.POST.get("image_alt")
        image = request.POST.get("testi-image")

        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.image = image_data
        data.name = name
        data.message = desc
        data.image_alt = image_alt
        data.save()

        messages.success(request, "Testimonial Updated Successfully...!!")
        return redirect("testimonial_view")


class CareerListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Career"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = VaccancyDetails.objects.all().order_by("-id")

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
                VaccancyDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = VaccancyDetails.objects.get(id=item_id)
                except VaccancyDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "career", "career_view", context)


class CareerCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def post(self, request, *args, **kwargs):
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        location = request.POST.get("location")
        salary = request.POST.get("salary")
        # cat_instance = request.POST.get('cat')
        # category = JobCategory.objects.get(id=cat_instance)
        types = request.POST.getlist("types")
        types_str = ", ".join(types)

        career = VaccancyDetails(
            salary=salary,
            type=types_str,
            title=name,
            description=desc,
            location=location,
        )
        career.save()

        messages.success(request, "Career Added Successfully...!!")
        return redirect("career_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = JobCategory.objects.filter(status=True).order_by("-id")
        return context


class CareerUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/career/career_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, id):
        data = VaccancyDetails.objects.get(pk=id)
        types_list = data.type.split(", ")
        # category = JobCategory.objects.filter(status=True)
        return render(
            request, self.template_name, {"list": data, "types_list": types_list}
        )

    def post(self, request, id):
        data = VaccancyDetails.objects.get(pk=id)
        # category = JobCategory.objects.filter(status=True)
        desc = request.POST.get("desc")
        name = request.POST.get("title")
        location = request.POST.get("location")
        salary = request.POST.get("salary")
        # cat_instance = request.POST.get('cat')
        # category = JobCategory.objects.get(id=cat_instance)

        types = request.POST.getlist("types")

        data.type = ", ".join(types)
        data.title = name
        # data.category = category
        data.location = location
        data.salary = salary
        data.description = desc
        data.save()
        messages.success(request, "Career Updated Successfully...!!")
        return redirect("career_view")


class ApplicationListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/application/application_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaHR"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "application"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        start_date = request.GET.get("start_date")  # Get start_date from request
        end_date = request.GET.get("end_date")  # Get end_date from request

        cd = ApplicationDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(
                    Q(first_name__icontains=search) | Q(job__icontains=search)
                )
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                ApplicationDetails.objects.filter(id=item_id).update(status=status)

            if start_date and end_date:  # Filter by date range if provided
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                cd = cd.filter(date__range=(start_date, end_date))

            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ApplicationDetails.objects.get(id=item_id)
                except ApplicationDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "application", "application_view", context)


class HistoryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "History"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = HistoryDetails.objects.all().order_by("-id")

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
                HistoryDetails.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = HistoryDetails.objects.get(id=item_id)
                except HistoryDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()
            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "history", "history_view", context)


class HistoryCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        year = request.POST.get("year")
        desc = request.POST.get("desc")
        image_alt = request.POST.get("image_alt")

        history = HistoryDetails(
            title=title, year=year, description=desc, image_alt=image_alt
        )
        history.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = HistoryImage(history=history, image=image)
            slider.save()
        messages.success(request, "History Added Successfully...!!")
        return redirect("history_view")


class HistoryUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/history/history_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = HistoryDetails.objects.get(pk=id)
        sliders = data.history_image.all()
        return render(request, self.template_name, {"list": data, "sliders": sliders})

    def post(self, request, id):
        data = HistoryDetails.objects.get(pk=id)
        sliders = data.history_image.all()
        title = request.POST.get("title")
        year = request.POST.get("year")
        desc = request.POST.get("desc")
        image_alt = request.POST.get("image_alt")

        data.title = title
        data.year = year
        data.description = desc
        data.image_alt = image_alt
        data.save()

        slider_images = request.FILES.getlist("files")
        for image in slider_images:
            slider = HistoryImage(history=data, image=image)
            slider.save()
        messages.success(request, "History Updated Successfully...!!")
        return redirect("history_view")


def delete_historyslider(request, image_id):
    try:
        # Get the image by its ID and delete it
        image = HistoryImage.objects.get(pk=image_id)
        image.image.delete()  # Delete the image file
        image.delete()  # Delete the database record
        return JsonResponse({"success": True})
    except EventGalleryImage.DoesNotExist:
        return JsonResponse({"success": False, "error": "Image not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


class ContactListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/contact/contact_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Contat"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = ContactUsDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(name__icontains=search)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = ContactUsDetails.objects.get(id=item_id)
                except ContactUsDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "contact", "contact_view", context)


class EnquiryListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/enquiry/enquiry_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "Enquiry"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")
        start = request.GET.get("start")
        end = request.GET.get("end")
        start_date = None
        end_date = None

        if start and end:
            start_date = datetime.strptime(start, "%m/%d/%Y").date()
            end_date = datetime.strptime(end, "%m/%d/%Y").date()

        cd = EnquiryDetails.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(
                    Q(name__icontains=search) | Q(created__range=(start, end))
                )
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = EnquiryDetails.objects.get(id=item_id)
                except EnquiryDetails.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            if start_date and end_date:
                cd = cd.filter(
                    created__date__gte=start_date, created__date__lte=end_date
                )

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path

        return renderhelper(request, "enquiry", "enquiry", context)


# excel export


class ExportExcel(View):
    def get(self, request):
        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            start = request.GET.get("start")
            end = request.GET.get("end")

            try:
                enquiries = EnquiryDetails.objects.filter(
                    created__gte=start, created__lte=end
                )
                enquiries_data = [
                    {
                        "product": enquiry.product,
                        "name": enquiry.name,
                        "location": enquiry.location,
                        "email": enquiry.email,
                        "mobile_no": enquiry.mobile_no,
                        "message": enquiry.message,
                        "created": enquiry.created.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for enquiry in enquiries
                ]
                return JsonResponse({"status": True, "enquiries": enquiries_data})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({"error": "Invalid request"}, status=400)


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

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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


class SupermarketListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/supermarket/supermarket_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "supermarket"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Supermarkets.objects.all().order_by("-id")

        if is_ajax(request):
            # if search:
            #     cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Supermarkets.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Supermarkets.objects.get(id=item_id)
                except Supermarkets.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        return renderhelper(request, "supermarket", "supermarket_view", context)


class SupermarketCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/supermarket/supermarket_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        image = request.POST.get("supermarket-image")
        image_alt = request.POST.get("image_alt")
        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        supermarket = Supermarkets.objects.create(image=image_data, image_alt=image_alt)
        messages.success(request, "Supermarket Added Successfully...!!")
        return redirect("supermarket_view")


class SupermarketUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/supermarket/supermarket_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Supermarkets.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Supermarkets.objects.get(pk=id)
        image = request.POST.get("supermarket-image")
        image_alt = request.POST.get("image_alt")
        if image:
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
            data.image = image_data
        data.image_alt = image_alt
        data.save()

        messages.success(request, "Supermarket Updated Successfully...!!")
        return redirect("supermarket_view")


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

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
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


class CertificationListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/certification/certification_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "certification"
        page = request.GET.get("page", 1)

        # search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Certification.objects.all().order_by("-id")

        if is_ajax(request):
            # if search:
            #     cd = cd.filter(name__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Certification.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Certification.objects.get(id=item_id)
                except Certification.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        return renderhelper(request, "certification", "certification_view", context)


class CertificationCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/certification/certification_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        # image = request.POST.get('certification-image')

        # format, imgstr = image.split(';base64,')
        # ext = format.split('/')[-1]
        # image_data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        # certification = Certification.objects.create(image=image_data)
        image = request.FILES.get("image")
        image_alt = request.POST.get("image_alt")
        certi = Certification(image=image, image_alt=image_alt)
        certi.save()
        messages.success(request, "Certification Added Successfully...!!")
        return redirect("certification_view")


class CertificationUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/certification/certification_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Certification.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Certification.objects.get(pk=id)
        # image = request.POST.get('certification-image')
        image = request.FILES.get("image")
        image_alt = request.POST.get("image_alt")

        if image:
            # format, imgstr = image.split(';base64,')
            # ext = format.split('/')[-1]
            # image_data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            data.image = image
        data.image_alt = image_alt
        data.save()

        messages.success(request, "Certification Updated Successfully...!!")
        return redirect("certification_view")


class AboutusListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/aboutus/aboutus_list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "aboutus"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Aboutus.objects.all().order_by("-id")

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
                Aboutus.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Aboutus.objects.get(id=item_id)
                except Aboutus.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        return renderhelper(request, "aboutus", "aboutus_view", context)


class AboutusCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/aboutus/aboutus_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        title = request.POST.get("title")

        about = Aboutus(image=image, title=title)
        about.save()
        messages.success(request, "About Us Added Successfully...!!")
        return redirect("about_view")


class AboutusUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/aboutus/aboutus_create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Aboutus.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Aboutus.objects.get(pk=id)
        image = request.FILES.get("image")
        title = request.POST.get("title")

        if image:
            data.image = image
        data.title = title
        data.save()

        messages.success(request, "About Us Updated Successfully...!!")
        return redirect("about_view")


class SeoListView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/seo/seo-list.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, *args, **kwargs):
        context = {}
        path = "seo"
        page = request.GET.get("page", 1)

        search = request.GET.get("search")
        delete = request.GET.get("delete")
        status = request.GET.get("status")
        sts = request.GET.get("sts")

        cd = Seo.objects.all().order_by("-id")

        if is_ajax(request):
            if search:
                cd = cd.filter(page__icontains=search)
            if sts:
                cd = cd.filter(status=sts)
            if status:
                if status == "1":
                    status = True
                else:
                    status = False
                item_id = request.GET.get("item_id")
                Seo.objects.filter(id=item_id).update(status=status)
            if delete:
                item_id = request.GET.get("item_id")
                try:
                    datas = Seo.objects.get(id=item_id)
                except Seo.DoesNotExist:
                    datas = None
                if datas:
                    datas.delete()

            paginator = Paginator(cd, PAGINATION_COUNT)
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

        paginator = Paginator(cd, PAGINATION_COUNT)
        try:
            datas = paginator.get_page(page)
        except PageNotAnInteger:
            datas = paginator.get_page(1)
        except EmptyPage:
            datas = paginator.get_page(paginator.num_pages)
        context["datas"] = datas
        context["page"] = page
        context["path"] = path
        return renderhelper(request, "seo", "seo-view", context)


class SeoCreateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/seo/seo-create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def post(self, request, *args, **kwargs):
        page = request.POST.get("page")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")

        seo = Seo(
            page=page,
            title_tag=title_tag,
            metatag=metatag,
            keyword=keyword,
            canonical=canonical,
        )
        seo.save()
        messages.success(request, "Seo Added Successfully...!!")
        return redirect("seo_view")


class SeoUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "superadmin/seo/seo-create.html"

    def test_func(self):
        return self.request.user.username == "DeepSeaAdmin"

    def get(self, request, id):
        data = Seo.objects.get(pk=id)
        return render(request, self.template_name, {"list": data})

    def post(self, request, id):
        data = Seo.objects.get(pk=id)
        page = request.POST.get("page")
        title_tag = request.POST.get("title_tag")
        metatag = request.POST.get("metatag")
        keyword = request.POST.get("keyword")
        canonical = request.POST.get("canonical")

        data.page = page
        data.title_tag = title_tag
        data.metatag = metatag
        data.keyword = keyword
        data.canonical = canonical
        data.save()

        messages.success(request, "Seo Updated Successfully...!!")
        return redirect("seo_view")
