from django.db import models

from company.models import StatusTimestampBase
from phonenumber_field.modelfields import PhoneNumberField


from multiselectfield import MultiSelectField
from datetime import date, timedelta


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
    hiring_status = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text="Status of the job's hiring process (e.g., 'Urgent Requirement')."
    )
    type = MultiSelectField(choices=JOB_TYPE_CHOICES, null=True, blank=True)
    salary = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vacancy Details"

    def __str__(self):
        return f"{self.title} - {self.category}"


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

    def __str__(self):
        return f"Job - {self.job} - {self.first_name}"

    def save(self, *args, **kwargs):
        if not self.start_date:
            notice_mapping = {
                "immediate": 0,
                "2_weeks": 14,
                "1_month": 30,
            }
            days = notice_mapping.get(self.notice_period, 0)
            self.start_date = date.today() + timedelta(days=days)
        super().save(*args, **kwargs)
