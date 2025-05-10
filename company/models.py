from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from accounts.models import User


def image_upload_path(instance, filename):
    """Here we are using uuid to generate a unique filename for the image.
    Because instance.id is None until the object is saved."""
    model_name = instance.__class__.__name__.lower()
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"{model_name}/{filename}"


class TimestampBase(models.Model):
    """Common base model for items with  timestamps"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageBase(models.Model):
    """Common base model for items with image"""

    image = models.ImageField(upload_to=image_upload_path, null=True)
    image_alt = models.CharField(
        max_length=125,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class StatusTimestampBase(TimestampBase):
    """Common base model for items with status"""

    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class BaseInfoModel(models.Model):
    """Common base model for items with title,location,date"""

    title = models.CharField(max_length=350)
    location = models.CharField(max_length=255)
    date = models.DateField(null=True)

    class Meta:
        abstract = True


class SEO(StatusTimestampBase):
    PAGE_NAME_CHOICES = [
        ("", "Select the Page"),
        ("/", "Home"),
        ("/about/", "About"),
        ("/brands/oceano", "Brand"),
        ("/product", "Products"),
        ("/career", "Career"),
        ("/contact", "Contact"),
        ("/blog", "Blogs"),
        ("/news-room", "News Room"),
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

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEOs"

    def __str__(self):
        return self.page_name

    def get_absolute_url(self):
        return reverse(self.page_name)


class Brand(StatusTimestampBase, ImageBase):
    name = models.CharField(max_length=100, blank=True)
    sequence = models.PositiveIntegerField(null=True)  # TODO Need to change

    def __str__(self):
        return self.name


class Event(StatusTimestampBase, BaseInfoModel):
    sequence = models.PositiveIntegerField(null=True)  # TODO Need to change
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class EventImage(StatusTimestampBase, ImageBase):
    event = models.ForeignKey(
        Event,
        null=False,
        related_name="event_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"

    def __str__(self):
        return f"{self.event.title} - Slider {self.pk}"


class News(StatusTimestampBase, BaseInfoModel):
    TYPE_CHOICES = (
        ("", "Select the Type"),
        ("company news", "Company News"),
        ("global news", "Global News"),
    )
    sequence = models.PositiveIntegerField(null=True)  # TODO Need to change
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    content = models.TextField(
        null=True
    )  # TODO Need to change to the one in the blog model
    slug = AutoSlugField(
        populate_from="name",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_details", kwargs={"slug": self.slug})


class NewsImage(TimestampBase, ImageBase):
    news = models.ForeignKey(
        News,
        null=False,
        related_name="news_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "News Image"
        verbose_name_plural = "News Images"

    def __str__(self):
        return f"{self.news.title} - Slider {self.pk}"


class Promotion(StatusTimestampBase, BaseInfoModel):
    """TODO Need to check if this field is used in the app"""

    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Promotion Details"


class PromotionImage(TimestampBase, ImageBase):
    promotion = models.ForeignKey(
        Promotion,
        null=False,
        related_name="promotion_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Promotion Image"
        verbose_name_plural = "Promotion Images"


class Blog(StatusTimestampBase, BaseInfoModel):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Detail"
        verbose_name_plural = "Blog Details"

    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"slug": self.slug})


class BlogImage(TimestampBase, ImageBase):
    blog = models.ForeignKey(
        Blog,
        null=False,
        related_name="blog_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Blog Image"
        verbose_name_plural = "Blog Images"


class ManagementTeam(StatusTimestampBase, ImageBase):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    sequence = models.PositiveIntegerField(null=True)  # TODO Need to change

    class Meta:
        verbose_name = "Management Team"
        verbose_name_plural = "Management Teams"


class CompanyTestimonial(StatusTimestampBase, ImageBase):
    name = models.CharField(max_length=350)
    quote = models.TextField()

    class Meta:
        verbose_name = "Company Testimonial"
        verbose_name_plural = "Company Testimonials"


class Certification(StatusTimestampBase, ImageBase):
    sequence = models.IntegerField(null=True, blank=True)  # TODO no change needed

    class Meta:
        ordering = ["sequence"]


class ContactUs(StatusTimestampBase):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    message = models.TextField(null=True)


class Supermarkets(StatusTimestampBase, ImageBase):
    sequence = models.IntegerField(null=True)  # TODO no change needed

    class Meta:
        ordering = ["sequence"]


class Enquiry(StatusTimestampBase):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    mobile_number = PhoneNumberField(blank=True)
    message = models.TextField(null=True)


class History(StatusTimestampBase):
    year = models.PositiveIntegerField(
        null=True, validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Histories"

    def __str__(self):
        return str(self.year)


class HistoryImage(StatusTimestampBase, ImageBase):  # active

    history = models.ForeignKey(
        History,
        null=False,
        related_name="history_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "History Image"
        verbose_name_plural = "History Images"
