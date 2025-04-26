import base64
import uuid
from django.core.files.base import ContentFile
from django import forms
from .models import (
    Product,
    Category,
    Brand,
    RecipeDetails,
    RecipeIngredients,
    ProductDetails,
)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["brand", "name", "sequence"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["brand"].queryset = Brand.objects.filter(status=True)
        self.fields["brand"].empty_label = "Select Brand"
        self.fields["brand"].widget.attrs.update(
            {"class": "form-control form-select select2", "required": "true"}
        )

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Name",
                "required": "true",
            }
        )

        self.fields["sequence"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Sequence",
                "required": "true",
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
            }
        )


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeDetails
        fields = [
            "title",
            "brand",
            "description",
            "image_alt",
        ]  # the description --need to check on that-- instructions
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image_alt": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["brand"].queryset = Brand.objects.filter(status=True).exclude(
            name="Deep Sea"
        )
        self.fields["brand"].widget.attrs.update(
            {"class": "form-control form-select select2"}
        )
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Title"}
        )


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ["title"]
        widgets = {
            "title": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Ingredient",
                    "rows": 2,
                }
            ),
        }


RecipeIngredientFormSet = forms.inlineformset_factory(
    RecipeDetails,
    RecipeIngredients,
    form=RecipeIngredientForm,
    extra=1,
    can_delete=True,
)


class ProductForm(forms.ModelForm):
    # replace the default FileField widget with a hidden text field
    image = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Product
        fields = [
            "brand", "sequence", "type", "name",
            "image_alt", "image", "homepage"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fname, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({"class": "form-check-input"})
            elif isinstance(widget, forms.HiddenInput):
                widget.attrs.update({"id": "cropped-img", "name": "image"})
            else:
                widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        instance = super().save(commit=False)
        data_url = self.cleaned_data.get("image")
        if data_url:
            header, b64data = data_url.split(";base64,")
            ext = header.split("/")[-1]  # e.g. "png"
            filename = f"{uuid.uuid4().hex}.{ext}"
            decoded_file = base64.b64decode(b64data)
            instance.image = ContentFile(decoded_file, name=filename)
        if commit:
            instance.save()
        return instance


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = [
            "product",
            "category",
            "sub_categories",
            "product_code",
            "net_weight",
            "price",
            "origin",
            "grade",
            "packing",
            "nutrition",
            "ingredients",
            "instructions",
            "storage_instructions",
            "allergic",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        deepsea_active_filters = {"status": True, "brand__name": "Deep Sea"}
        self.fields["product"].queryset = Product.objects.filter(
            **deepsea_active_filters
        ).order_by("-id")
        self.fields["category"].queryset = Category.objects.filter(
            **deepsea_active_filters
        ).order_by("-id")

        for name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, forms.Select):
                widget.attrs.update(
                    {
                        "class": "select-drop",
                        "required": True,
                    }
                )

            elif isinstance(widget, forms.Textarea):
                widget.attrs.update(
                    {
                        "class": "form-control",
                        "placeholder": field.label or name.replace("_", " ").title(),
                    }
                )

            else:
                widget.attrs.update(
                    {
                        "class": "form-control",
                        "placeholder": field.label or name.replace("_", " ").title(),
                    }
                )

        self.fields["product"].label = "Product*"
        self.fields["category"].label = "Category*"


class BrandProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "sequence", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            widget = self.fields[field].widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({"class": "form-check-input"})
            elif isinstance(widget, forms.Select):
                widget.attrs.update({"class": "select-drop"})
            else:
                widget.attrs.update({"class": "form-control"})


class BrandProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = [
            "product",
            "category",
            "net_weight",
            "origin",
            "instructions",
            "shelf_life",
            "how_to_cook",
            "ingredients",
            "allergic",
            "nutrition",
        ]
        widgets = {
            "net_weight": forms.TextInput(attrs={"placeholder": "Net weight"}),
            "origin": forms.TextInput(attrs={"placeholder": "Country of origin"}),
            "instructions": forms.Textarea(attrs={"placeholder": "Storage instructions"}),
            "shelf_life": forms.TextInput(attrs={"placeholder": "Shelf life"}),
            "how_to_cook": forms.Textarea(
                attrs={"placeholder": "Cooking instructions"}
            ),
            "ingredients": forms.Textarea(attrs={"placeholder": "List of ingredients"}),
            "allergic": forms.Textarea(attrs={"placeholder": "Allergen information"}),
            "nutrition": forms.Textarea(attrs={"placeholder": "Nutrition facts"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({"class": "form-check-input"})
            elif isinstance(widget, forms.Select):
                widget.attrs.update({"class": "select-drop"})
            else:
                widget.attrs.update({"class": "form-control"})
