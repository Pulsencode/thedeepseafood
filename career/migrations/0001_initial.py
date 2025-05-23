# Generated by Django 5.2 on 2025-05-16 07:30

import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Job categories",
            },
        ),
        migrations.CreateModel(
            name="VacancyDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                ("title", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=255)),
                ("description", models.TextField(null=True)),
                (
                    "hiring_status",
                    models.CharField(
                        blank=True,
                        help_text="Status of the job's hiring process (e.g., 'Urgent Requirement').",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "type",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("full time", "Full-Time"),
                            ("part time", "Part-Time"),
                            ("remote", "Remote"),
                            ("hybrid", "Hybrid"),
                        ],
                        max_length=33,
                        null=True,
                    ),
                ),
                ("salary", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_category",
                        to="career.jobcategory",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Vacancy Details",
            },
        ),
        migrations.CreateModel(
            name="ApplicationDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                (
                    "notice_period",
                    models.CharField(
                        choices=[
                            ("", "Select any"),
                            ("immediate", "Immediate Join"),
                            ("2_weeks", "2 Weeks"),
                            ("1_month", "1 Month"),
                        ],
                        max_length=100,
                    ),
                ),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                ("portfolio_url", models.URLField(blank=True, null=True)),
                ("date_of_birth", models.DateField(null=True)),
                ("message", models.TextField(blank=True, null=True)),
                ("upload_cv", models.FileField(upload_to="cv")),
                (
                    "cover_letter",
                    models.FileField(blank=True, null=True, upload_to="cover_letter"),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="career.vacancydetails",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Application Details",
            },
        ),
    ]
