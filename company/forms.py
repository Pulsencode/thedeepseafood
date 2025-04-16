from django import forms
from company.models import CompanyTestimonial, AboutUs, ManagementTeam


class CompanyTestimonialForm(forms.ModelForm):
    class Meta:
        model = CompanyTestimonial
        fields = "__all__"


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"


class ManagementTeamForm(forms.ModelForm):
    class Meta:
        model = ManagementTeam
        fields = "__all__"
