from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class TimestampBase(models.Model):
    """
        Common base model for items with  timestamps.
    .
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusTimestampBase(TimestampBase):
    """
        Common base model for items with status and timestamps.
    .
    """

    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Certification(StatusTimestampBase):
    image = models.ImageField(upload_to="certification", null=True)


class Supermarkets(StatusTimestampBase):
    images = models.ImageField(upload_to="supermarkets", null=True)

    class Meta:
        verbose_name_plural = "Supermarkets"


class AboutUs(StatusTimestampBase):
    image = models.ImageField(upload_to="about_us", null=True)
    title = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self) -> str:
        return self.title


class CompanyTestimonial(StatusTimestampBase):
    name = models.TextField(null=True)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="testimonials", null=True)


class Brand(StatusTimestampBase):
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    logo = models.FileField(upload_to="brand", null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class SEO(models.Model):
    PAGE_NAME_CHOICES = [
        ("hm", "Home"),
        ("abt", "About"),
        ("svc", "Services"),
        ("prd", "Products"),
        ("car", "Career"),
        ("con", "Contact"),
        ("blg", "Blogs"),
        ("nws", "News"),
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


class ManagementTeam(StatusTimestampBase):
    designation = models.TextField(null=True)
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="management_team", null=True)

    def __str__(self):
        return self.name


class HistoryDetails(StatusTimestampBase):
    year = models.TextField(null=True)
    title = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):

        return self.year


class HistoryImage(TimestampBase):
    history = models.ForeignKey(
        HistoryDetails,
        null=False,
        related_name="history_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="history", null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)


class BlogDetails(StatusTimestampBase):
    title = models.TextField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)
    slug = AutoSlugField(
        populate_from="title", null=True, blank=True, unique=True, max_length=255
    )

    class Meta:
        verbose_name_plural = "Blog Details"

    def __str__(self):
        return self.title


class BlogImage(TimestampBase):
    blog = models.ForeignKey(BlogDetails, on_delete=models.CASCADE,related_name="blog_image")
    image = models.ImageField(upload_to="blog")


class NewsDetails(
    StatusTimestampBase
):  # assuming StatusTimestampBase is already optimized
    title = models.CharField(max_length=255, null=True, blank=True)
    sequence = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title or "Untitled News"

    class Meta:
        verbose_name_plural = "News Details"


class NewsGalleryImage(models.Model):
    news = models.ForeignKey(
        NewsDetails,
        related_name="news_images",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="news/", null=True, blank=True)

    def __str__(self):
        return f"{self.news.title or 'Untitled'} - Image {self.pk}"


class EventGallery(StatusTimestampBase):
    title = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title


class EventGalleryImage(TimestampBase):
    event = models.ForeignKey(
        EventGallery,
        null=False,
        related_name="gallery_image",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="event_gallery", null=True)
    is_active = models.BooleanField(null=False, blank=True, default=True)

    def __str__(self):
        return f"{self.event.title} - Slider {self.pk}"


class PromotionDetails(StatusTimestampBase):
    title = models.TextField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Promotion Details"


class PromotionImage(TimestampBase):
    promotion = models.ForeignKey(
        PromotionDetails,
        null=False,
        related_name="promotion",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="promotion", null=True)
