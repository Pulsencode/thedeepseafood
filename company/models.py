from django.db import models

from autoslug import AutoSlugField


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

    def _str_(self):
        return self.page


class Brand(models.Model):
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    logo = models.FileField(upload_to="brandimg", null=True, blank=True)
    image_alt = models.TextField(null=True, blank=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self) -> str:
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

    def _str_(self):
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

    def _str_(self):
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

    def _str_(self):
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

    def _str_(self):
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

    def _str_(self):
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


class Certification(models.Model):
    image = models.ImageField(upload_to="certificationimg", null=True)
    image_alt = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True)
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
