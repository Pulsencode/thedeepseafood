from django import forms
from career.models import VacancyDetails, JobCategory
from career.models import ApplicationDetails


class VacancyDetailForm(forms.ModelForm):
    class Meta:
        model = VacancyDetails
        fields = "__all__"


class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = "__all__"


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
            "message": forms.Textarea(attrs={"rows": 4}),
            "notice_period": forms.Select(
                choices=ApplicationDetails.NOTICE_PERIOD_CHOICES
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_of_birth"].input_formats = ["%Y-%m-%d"]
        self.fields["phone_number"].widget.attrs.update({
            "onkeypress": "return event.charCode >= 48 && event.charCode <= 57"
        })
        original = [
            (val, label)
            for val, label in self.fields["notice_period"].choices
            if val != ""
        ]
        self.fields["notice_period"].choices = [
            ("", "Select any")
        ] + original
        for fname, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.FileInput):
                widget.attrs.update({"class": ""})
            else:
                widget.attrs.update({"class": "form-control"})

    def clean_upload_cv(self):
        upload_cv = self.cleaned_data.get("upload_cv")
        if upload_cv and not upload_cv.name.lower().endswith('.pdf'):
            raise forms.ValidationError("Only PDF files are allowed.")
        return upload_cv

    def clean_cover_letter(self):
        cover_letter = self.cleaned_data.get("cover_letter")
        if cover_letter and not cover_letter.name.lower().endswith('.pdf'):
            raise forms.ValidationError("Only PDF files are allowed.")
        return cover_letter
