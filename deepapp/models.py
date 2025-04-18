from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, password2=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# custom user model


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Brand(models.Model):
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    logo = models.FileField(upload_to="brandimg", null=True, blank=True)
    image_alt = models.TextField(null=True, blank=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    image = models.FileField(upload_to="categoryimg", null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class JobCategory(models.Model):
    name = models.TextField(null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class EventGallery(models.Model):
    title = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EventGalleryImage(models.Model):
    event = models.ForeignKey(
        EventGallery,
        null=False,
        related_name="gallery_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="galleryimg", null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event.title} - Slider {self.pk}"


class NewsDetails(models.Model):
    title = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    type = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)
    title_tag = models.TextField(null=True)
    metatag = models.TextField(null=True)
    keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NewsGalleryImage(models.Model):
    news = models.ForeignKey(
        NewsDetails,
        null=False,
        related_name="news_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="newsimg", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.news.title} - Slider {self.pk}"


class PromotionDetails(models.Model):
    title = models.TextField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PromotionImage(models.Model):
    promotion = models.ForeignKey(
        PromotionDetails,
        null=False,
        related_name="promo_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="promotionimg", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BlogDetails(models.Model):
    title = models.TextField(null=True)
    slug = AutoSlugField(
        populate_from="title", null=True, blank=True, unique=True, max_length=255
    )
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)
    title_tag = models.TextField(null=True)
    metatag = models.TextField(null=True)
    keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title and (not self.slug or self.slug != self.title):
            self.slug = AutoSlugField(populate_from="title", unique=True).slugify(
                self.title
            )
        super(BlogDetails, self).save(*args, **kwargs)


class BlogImage(models.Model):
    blog = models.ForeignKey(
        BlogDetails,
        null=False,
        related_name="blog_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="blogimg", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ManagementTeam(models.Model):
    designation = models.TextField(null=True)
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="teamimg", null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CompanyTestimonial(models.Model):
    name = models.TextField(null=True)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="testimonialimg", null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class VaccancyDetails(models.Model):
    category = models.ForeignKey(
        JobCategory,
        null=True,
        blank=True,
        related_name="job_category",
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True)
    location = models.TextField(null=True)
    description = models.TextField(null=True)
    type = models.TextField(null=True)
    salary = models.TextField(null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class HistoryDetails(models.Model):
    year = models.TextField(null=True)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class HistoryImage(models.Model):
    history = models.ForeignKey(
        HistoryDetails,
        null=False,
        related_name="history_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="historyimg", null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ContactUsDetails(models.Model):
    name = models.TextField(null=True)
    location = models.TextField(null=True)
    email = models.EmailField(null=True, blank=True)
    mobile_no = models.TextField(null=True)
    message = models.TextField(null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Supermarkets(models.Model):
    image = models.ImageField(upload_to="supermarketsimg", null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class EnquiryDetails(models.Model):
    product = models.TextField(null=True)
    name = models.TextField(null=True)
    location = models.TextField(null=True)
    email = models.EmailField(null=True, blank=True)
    mobile_no = models.TextField(null=True)
    message = models.TextField(null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RecipeDetails(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
        related_name="rec_ind",
    )
    title = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.recipe.title


class RecipeImage(models.Model):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
        related_name="rec_image",
    )
    image = models.ImageField(upload_to="recipeimg", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.recipe.title


class Product(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="product_brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    type = models.TextField(null=True)
    slug_product = models.SlugField(
        default="", editable=False, null=True, blank=True, max_length=250
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to="productimg", null=True)
    title_tag = models.TextField(null=True)
    metatag = models.TextField(null=True)
    keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    homepage = models.BooleanField(null=False, blank=True, default=False)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def title_changed(self):
        if self.id:
            original = Product.objects.get(pk=self.id)
            return self.name != original.name
        return False


class ProductDetails(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_details", null=True, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="product_category",
        on_delete=models.CASCADE,
    )
    sub_categories = models.TextField(null=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    product_code = models.CharField(max_length=100, null=True, blank=True)
    net_weight = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # used as nutrition facts
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    storage_instructions = models.TextField(null=True, blank=True)
    shelf_life = models.TextField(null=True, blank=True)
    how_to_cook = models.TextField(null=True, blank=True)
    causion = models.TextField(
        null=True, blank=True
    )  # Caution is used as the allergen Information
    grade = models.CharField(max_length=2000, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    packing = models.CharField(max_length=2000, null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)

    def __str__(self) -> str:
        return self.product.name


class ApplicationDetails(models.Model):
    vaccancy = models.ForeignKey(
        VaccancyDetails,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    start_date = models.DateField(null=True, blank=True)
    job = models.TextField(null=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.TextField(null=True)
    mobile_no = models.TextField(null=True)
    notice = models.TextField(null=True)
    linkedin = models.TextField(null=True)
    portfolio = models.TextField(null=True)
    date = models.DateField(null=True)

    message = models.TextField(null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    cover = models.FileField(upload_to="careerfiles", null=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Subcategory(models.Model):
    name = models.TextField(null=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Certification(models.Model):
    image = models.ImageField(upload_to="certificationimg", null=True)
    image_alt = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Aboutus(models.Model):
    image = models.ImageField(upload_to="aboutusimg", null=True)
    title = models.TextField(null=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Seo(models.Model):
    page = models.TextField(null=True, blank=True)
    title_tag = models.TextField(null=True)
    metatag = models.TextField(null=True)
    keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page
