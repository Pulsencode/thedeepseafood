from django.db import models

from company.models import Brand


class Category(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    image = models.FileField(upload_to="categoryimg", null=True)

    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class RecipeDetails(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
        related_name="rec_ind",
    )
    title = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.recipe.title


class Product(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="product_brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    type = models.TextField(null=True)
    slug_product = models.SlugField(
        default="", editable=False, null=True, blank=True, max_length=250
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to="productimg", null=True)
    title_tag = models.TextField(null=True)
    metatag = models.TextField(null=True)
    keyword = models.TextField(null=True)
    canonical = models.TextField(null=True)
    image_alt = models.TextField(null=True, blank=True)
    homepage = models.BooleanField(null=False, blank=True, default=False)
    status = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def title_changed(self):
        if self.id:
            original = Product.objects.get(pk=self.id)
            return self.name != original.name
        return False


class ProductDetails(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_details", null=True, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="product_category",
        on_delete=models.CASCADE,
    )
    sub_categories = models.TextField(null=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    product_code = models.CharField(max_length=100, null=True, blank=True)
    net_weight = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # used as nutrition facts
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    storage_instructions = models.TextField(null=True, blank=True)
    shelf_life = models.TextField(null=True, blank=True)
    how_to_cook = models.TextField(null=True, blank=True)
    causion = models.TextField(
        null=True, blank=True
    )  # Caution is used as the allergen Information
    grade = models.CharField(max_length=2000, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True)
    packing = models.CharField(max_length=2000, null=True, blank=True)
    status = models.BooleanField(null=False, blank=True, default=True)

    def __str__(self) -> str:
        return self.product.name


class RecipeImage(models.Model):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
        related_name="rec_image",
    )
    image = models.ImageField(upload_to="recipeimg", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.recipe.title


class Subcategory(models.Model):
    name = models.TextField(null=True)

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
