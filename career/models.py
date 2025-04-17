from django.db import models

from company.models import StatusTimestampBase


class JobPosting(StatusTimestampBase):
    category = models.TextField(null=True)  # IT ,marketing
    status = models.BooleanField(null=False, blank=True, default=True)
    title = models.TextField(null=True)
    location = models.TextField(null=True)
    description = models.TextField(null=True)
    job_type = models.TextField(null=True)  # Hybrid,full time
    salary = models.TextField(null=True)


class ApplicationDetails(StatusTimestampBase):
    NOTICE_PERIOD_CHOICES = [
        ("immediate", "Immediate Join"),
        ("2_weeks", "2 Weeks"),
        ("1_month", "1 Month"),
    ]

    start_date = models.DateField(null=True, blank=True)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, null=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    notice_period = models.CharField(
        max_length=100, choices=NOTICE_PERIOD_CHOICES, null=True
    )
    linkedin_url = models.TextField(null=True)
    portfolio_url = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)

    message = models.TextField(null=True, blank=True)
    upload_cv = models.FileField(upload_to="cv", null=True)
    cover_letter = models.FileField(upload_to="cover_letter", null=True)
