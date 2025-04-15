from django.db import models

from autoslug import AutoSlugField


class StatusTimestampBase(models.Model):
    """
        Common base model for items with status and timestamps.
    .
    """

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Certification(StatusTimestampBase):
    image = models.ImageField(upload_to="certification", null=True)


class Supermarkets(StatusTimestampBase):
    images = models.ImageField(upload_to="supermarkets", null=True)


class AboutUs(StatusTimestampBase):
    image = models.ImageField(upload_to="about_us", null=True)
    title = models.TextField(null=True)

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


class SEO(StatusTimestampBase):
    PAGE = (
        ("/", "Home"),
        ("/blog/", "Blog"),
        ("/products/", "Products"),
        ("/career/", "Career"),
        ("/about/", "About"),
        ("/news-room/", "NewsRoom"),
    )
    page = models.CharField(max_length=150, choices=PAGE, null=True)
    meta_title = models.TextField(null=True)
    meta_tag = models.TextField(null=True)
    meta_keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.page


class ManagementTeam(StatusTimestampBase):
    designation = models.TextField(null=True)
    name = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="management_team", null=True)

    def __str__(self):
        return self.name


class HistoryDetails(models.Model):
    year = models.TextField(null=True)
    title = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):

        return self.year


class BlogDetails(models.Model):
    title = models.TextField(null=True)
    slug = AutoSlugField(
        populate_from="title", null=True, blank=True, unique=True, max_length=255
    )
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title


class NewsDetails(models.Model):
    title = models.TextField(null=True)
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    type = models.TextField(null=True)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title


# class Seo(models.Model):
#     page = models.TextField(null=True,blank=True)
#     title_tag = models.TextField(null=True)
#     metatag = models.TextField(null=True)
#     keyword = models.TextField(null=True)
#     canonical = models.TextField(null=True)
#     status = models.BooleanField( default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.page
# class CompanyTestimonial(models.Model):
#     name = models.TextField( null=True)
#     message = models.TextField(null=True)
#     image = models.ImageField(upload_to='testimonialimg',null=True)
#     image_alt = models.TextField(null=True,blank=True)
#     status = models.BooleanField(null=False, blank=True, default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

# class Aboutus(models.Model):
#     image = models.ImageField(upload_to='aboutusimg',null=True)
#     title = models.TextField(null=True)

#     status = models.BooleanField( default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class BlogDetails(models.Model):
#     title = models.TextField(null=True)
#     slug= AutoSlugField(populate_from='title', null=True, blank=True,unique=True,max_length=255)
#     name = models.TextField(null=True)
#     description = models.TextField(null=True)
#     location = models.TextField(null=True)
#     date = models.DateField(null=True)
#     title_tag = models.TextField(null=True)
#     metatag = models.TextField(null=True)
#     keyword = models.TextField(null=True)
#     canonical = models.TextField(null=True)
#     image_alt = models.TextField(null=True,blank=True)

#     status = models.BooleanField(null=False, blank=True, default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if self.title and (not self.slug or self.slug != self.title):
#             self.slug = AutoSlugField(populate_from='title', unique=True).slugify(self.title)
#         super(BlogDetails, self).save(*args, **kwargs)


# class BlogImage(models.Model):
#     blog = models.ForeignKey(
#         BlogDetails,
#         null=False,
#         related_name="blog_image",
#         on_delete=models.CASCADE,
#     )
#     image = models.ImageField(upload_to='blogimg',null=True)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Certification(models.Model):
#     image = models.ImageField(upload_to='certificationimg',null=True)
#     image_alt = models.TextField(null=True,blank=True)

#     status = models.BooleanField( default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Supermarkets(models.Model):
#     image = models.ImageField(upload_to='supermarketimg',null=True)
#     image_alt = models.TextField(null=True,blank=True)
#     status = models.BooleanField(null=False, blank=True, default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Aboutus(models.Model):
#     image = models.ImageField(upload_to='aboutusimg',null=True)
#     title = models.TextField(null=True)

#     status = models.BooleanField( default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class ManagementTeam(models.Model):
#     designation = models.TextField(null=True)
#     name = models.TextField(null=True)
#     sequence = models.PositiveIntegerField(null=True)
#     image = models.ImageField(upload_to='teamimg',null=True)
#     image_alt = models.TextField(null=True,blank=True)
#     status = models.BooleanField(null=False, blank=True, default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
