from django import forms
from career.models import VacancyDetails, JobCategory


class VacancyDetailForm(forms.ModelForm):
    class Meta:
        model = VacancyDetails
        fields = "__all__"


class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = "__all__"
