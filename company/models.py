from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator


def image_upload_path(instance, filename):
    model_name = instance.__class__.__name__.lower()
    obj_id = instance.id if instance.id else "temp"
    return f"{model_name}/{obj_id}/{filename}"


class TimestampBase(models.Model):
    """
        Common base model for items with  timestamps.
    .
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageBase(models.Model):
    """
        Common base model for items with image
    .
    """

    image = models.ImageField(upload_to=image_upload_path, null=True)

    class Meta:
        abstract = True


class StatusTimestampBase(TimestampBase):
    """
        Common base model for items with status
    .
    """

    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AboutUs(StatusTimestampBase, ImageBase):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "About Us"


class SEO(StatusTimestampBase):
    PAGE_NAME_CHOICES = [
        ("hm", "Home"),
        ("abt", "About"),
        ("brd", "Brand"),
        ("prd", "Products"),
        ("car", "Career"),
        ("con", "Contact"),
        ("blg", "Blogs"),
        ("nws", "News Room"),
    ]
    page_name = models.CharField(max_length=20, choices=PAGE_NAME_CHOICES, unique=True)
    meta_title = models.CharField(max_length=100)
    meta_author = models.CharField(max_length=100)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255, blank=True)
    meta_json_ld = models.TextField(blank=True)
    slug = AutoSlugField(
        populate_from="page_name",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.page_name

    def get_absolute_url(self):
        return reverse(self.page_name)


class Brand(StatusTimestampBase):
    name = models.CharField(max_length=100, null=True)
    sequence = models.PositiveIntegerField(null=True)
    logo = models.ImageField(upload_to=image_upload_path)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class EventGallery(StatusTimestampBase):
    title = models.CharField(max_length=350)
    sequence = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255)
    date = models.DateField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class EventGalleryImage(StatusTimestampBase, ImageBase):  # is active
    event = models.ForeignKey(
        EventGallery,
        null=False,
        related_name="gallery_image",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.event.title} - Slider {self.pk}"


class NewsDetails(StatusTimestampBase):
    TYPE = (("company news", "Company News"), ("global news", "Global News"))
    title = models.CharField(max_length=350)
    sequence = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255)
    date = models.DateField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title or "Untitled News"

    class Meta:
        verbose_name_plural = "News Details"


class NewsGalleryImage(TimestampBase, ImageBase):
    news = models.ForeignKey(
        NewsDetails,
        null=False,
        related_name="news_image",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.news.title} - Slider {self.pk}"


class PromotionDetails(StatusTimestampBase):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Promotion Details"


class PromotionImage(TimestampBase, ImageBase):
    promotion = models.ForeignKey(
        PromotionDetails,
        null=False,
        related_name="promotion_image",
        on_delete=models.CASCADE,
    )


class BlogDetails(StatusTimestampBase):
    title = models.CharField(max_length=350)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    location = models.CharField(max_length=255)
    date = models.DateField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blog Details"


class BlogImage(TimestampBase, ImageBase):
    blog = models.ForeignKey(
        BlogDetails,
        null=False,
        related_name="blog_image",
        on_delete=models.CASCADE,
    )


class ManagementTeam(StatusTimestampBase, ImageBase):
    role = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    sequence = models.PositiveIntegerField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )


class CompanyTestimonial(StatusTimestampBase, ImageBase):
    name = models.CharField(max_length=350)
    message = models.TextField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )


class Certification(StatusTimestampBase, ImageBase):
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )


class ContactUsDetails(StatusTimestampBase):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    message = models.TextField(null=True)


# active


class Supermarkets(StatusTimestampBase, ImageBase):
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )


class EnquiryDetails(StatusTimestampBase):  # active
    product = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    mobile_no = PhoneNumberField(blank=True)
    message = models.TextField(null=True)


class HistoryDetails(StatusTimestampBase):
    year = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )


class HistoryImage(StatusTimestampBase, ImageBase):  # active
    history = models.ForeignKey(
        HistoryDetails,
        null=False,
        related_name="history_image",
        on_delete=models.CASCADE,
    )
