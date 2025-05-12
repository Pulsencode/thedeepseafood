from django import forms

from company.models import ContactUs


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "phone_number", "email", "location", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 2}
            )
