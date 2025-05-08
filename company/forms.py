from django import forms
from company.models import (
    SEO,
    ManagementTeam,
    CompanyTestimonial,
    Supermarkets,
    Certification,
    Brand,
    News,
    Event,
    History,
    Promotion,
    Blog,
)
from django_summernote.widgets import SummernoteWidget


class SEOForm(forms.ModelForm):
    class Meta:
        model = SEO
        fields = [
            "page_name",
            "meta_title",
            "meta_author",
            "meta_description",
            "meta_keywords",
            "meta_json_ld",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class ManagementForm(forms.ModelForm):
    class Meta:
        model = ManagementTeam
        fields = ["image", "name", "sequence", "role", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = CompanyTestimonial
        fields = ["name", "quote", "image", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
        for field_name, field in self.fields.items():
            if field_name == "image":
                field.widget.attrs.update({"class": "item-img5 file center-block"})
            else:
                field.widget.attrs.update(
                    {"class": "form-control", "rows": 4, "placeholder": field.label}
                )


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ["image", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )


class SupermarketForm(forms.ModelForm):
    class Meta:
        model = Supermarkets
        fields = ["image", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "image", "sequence", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["name", "content", "title", "location", "date"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "content": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ["name", "location", "date", "description", "title"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "description": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ["year", "title", "description"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "description": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["sequence", "name", "description", "location", "date", "title"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "description": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["type", "name", "content", "sequence", "title", "location", "date"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "content": SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label, "rows": 4}
            )
