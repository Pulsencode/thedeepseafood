from django.db import models

# from autoslug import AutoSlugField


class SEO(models.Model):
    page = models.TextField(null=True, blank=True)
    meta_title = models.TextField(null=True)
    meta_tag = models.TextField(null=True)
    meta_keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_alt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.page


class CompanyTestimonial(models.Model):
    name = models.TextField(null=True)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="testimonial_img", null=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AboutUs(models.Model):
    image = models.ImageField(upload_to="aboutUs_img", null=True)
    title = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


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
