from django import forms
from django_summernote.widgets import SummernoteWidget

from career.models import ApplicationDetails, JobCategory, VacancyDetails


class VacancyDetailForm(forms.ModelForm):
    class Meta:
        model = VacancyDetails
        fields = [
            "title",
            "location",
            "description",
            "type",
            "salary",
            "hiring_status",
            "category",
        ]

        widgets = {
            "description": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(
                field.widget,
                (forms.TextInput, forms.NumberInput, forms.Select, forms.Textarea),
            ):
                field.widget.attrs.update(
                    {"class": "form-control", "placeholder": field.label, "rows": 1}
                )
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})


class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "placeholder": "Name"}
            )


class ApplicationDetailsForm(forms.ModelForm):
    honey = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ApplicationDetails
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "notice_period",
            "linkedin_url",
            "portfolio_url",
            "date_of_birth",
            "message",
            "upload_cv",
            "cover_letter",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone_number"].widget.attrs.update(
            {"id": "id_phone_number_application"}
        )
        for fname, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.FileInput):
                widget.attrs.update({"class": ""})
            else:
                widget.attrs.update({"class": "form-control", "rows": 4})

    def clean(self):
        cleaned_data = super().clean()
        upload_cv = cleaned_data.get("upload_cv")
        cover_letter = cleaned_data.get("cover_letter")

        for file_field, file_value in [
            ("upload_cv", upload_cv),
            ("cover_letter", cover_letter),
        ]:
            if file_value and not file_value.name.lower().endswith(".pdf"):
                self.add_error(file_field, "Only PDF files are allowed.")

        return cleaned_data
