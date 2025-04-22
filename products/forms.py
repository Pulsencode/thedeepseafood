from django import forms
from .models import Category, Brand, RecipeDetails, RecipeIngredients


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['brand', 'name', 'sequence']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['brand'].queryset = Brand.objects.filter(status=True)
        self.fields['brand'].empty_label = "Select Brand"
        self.fields['brand'].widget.attrs.update({
            'class': 'form-control form-select select2',
            'required': 'true'
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Category Name',
            'required': 'true'
        })

        self.fields['sequence'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Sequence',
            'required': 'true',
            'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'
        })


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeDetails
        fields = ['title', 'brand', 'description', 'image_alt']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_alt': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.filter(status=True).exclude(name="Deep Sea")
        self.fields['brand'].widget.attrs.update({'class': 'form-control form-select select2'})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['title']
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Ingredient',
                'rows': 2
            }),
        }


RecipeIngredientFormSet = forms.inlineformset_factory(
        RecipeDetails,
        RecipeIngredients,
        form=RecipeIngredientForm,
        extra=1,
        can_delete=True
    )
