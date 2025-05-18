from django import forms

from .models import Brand, Category, Product, ProductDetails


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["brand", "name", "sequence"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["brand"].queryset = Brand.objects.filter(status=True)
        self.fields["brand"].empty_label = "Select Brand"

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "placeholder": self.fields[field].label}
            )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "image", "sequence", "type", "image_alt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fname, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.HiddenInput):
                widget.attrs.update({"id": "cropped-img", "name": "image"})
            else:
                if not isinstance(widget, forms.CheckboxInput):
                    widget.attrs.update(
                        {"class": "form-control", "placeholder": field.label}
                    )


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
            "shelf_life",
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
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update(
                {"class": "form-control", "rows": 4, "placeholder": field.label}
            )


class BrandProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sequence", "image_alt"]

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
            "instructions": forms.Textarea(
                attrs={"placeholder": "Storage instructions"}
            ),
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
