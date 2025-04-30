from django.db import models

from company.models import StatusTimestampBase
from phonenumber_field.modelfields import PhoneNumberField


from multiselectfield import MultiSelectField


class JobCategory(StatusTimestampBase):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Job categories"

    def __str__(self):
        return self.name


class VacancyDetails(StatusTimestampBase):
    JOB_TYPE_CHOICES = (
        ("full time", "Full-Time"),
        ("part time", "Part-Time"),
        ("remote", "Remote"),
        ("contract", "Contract"),
    )
    category = models.ForeignKey(
        JobCategory,
        null=True,
        blank=True,
        related_name="job_category",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True)
    type = MultiSelectField(choices=JOB_TYPE_CHOICES, null=True, blank=True)
    salary = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Vacancy Details"


class ApplicationDetails(StatusTimestampBase):
    vacancy = models.ForeignKey(
        VacancyDetails,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    NOTICE_PERIOD_CHOICES = [
        ("immediate", "Immediate Join"),
        ("2_weeks", "2 Weeks"),
        ("1_month", "1 Month"),
    ]

    start_date = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)
    notice_period = models.CharField(
        max_length=100,
        choices=NOTICE_PERIOD_CHOICES,
    )
    linkedin_url = models.URLField(null=True)
    portfolio_url = models.URLField(null=True)
    date_of_birth = models.DateField(null=True)

    message = models.TextField(null=True, blank=True)
    upload_cv = models.FileField(upload_to="cv")
    cover_letter = models.FileField(upload_to="cover_letter")

    class Meta:
        verbose_name_plural = "Application Details"
