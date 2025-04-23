from django import forms
from company.models import (
    SEO,
    ManagementTeam,
    CompanyTestimonial,
    Supermarkets,
    Certification,
    Brand,
    News,
    NewsImage,
    Event,
    EventImage,
    History,
    HistoryImage,
    Promotion,
    PromotionImage,
    Blog,
    BlogImage,
)

from django.forms import inlineformset_factory

class SEOForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = SEO

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class ManagementForm(forms.ModelForm):
    class Meta:
        model = ManagementTeam
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = CompanyTestimonial
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class SupermarketForm(forms.ModelForm):
    class Meta:
        model = Supermarkets
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs.update({"class": "form-check-input"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control"})


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
                'date': forms.DateInput(attrs={
                    'type': 'date',
                    'class': 'form-control',  
                }),
            }


BlogImageFormSet = inlineformset_factory(
    Blog,
    BlogImage,
    fields=('image',),
    extra=1,  # Number of empty forms to display
    can_delete=False,
)

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__"


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
