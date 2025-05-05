from django import forms

from company.models import ContactUs


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "phone_number", "email", "location", "message"]
