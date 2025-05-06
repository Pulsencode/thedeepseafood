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
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = CompanyTestimonial
        fields = ["name", "quote", "image", "image_alt"]
        widgets = {
            "quote": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
        for field in self.fields:
            if field == "image":
                self.fields[field].widget.attrs.update(
                    {"class": "item-img5 file center-block"}
                )
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ["sequence", "image", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


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
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
