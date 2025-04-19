from django.db import models

# Create your models here.


class JobCategory(models.Model):
    name = models.TextField(null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


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
