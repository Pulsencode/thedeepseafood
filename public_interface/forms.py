from django import forms
from career.models import ApplicationDetails


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationDetails
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "date_of_birth",
            "notice_period",
            "linkedin_url",
            "portfolio_url",
            "message",
            "upload_cv",
            "cover_letter",
        ]
