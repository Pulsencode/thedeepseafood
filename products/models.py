from django.db import models
from company.models import Brand, StatusTimestampBase, ImageBase, TimestampBase
from autoslug import AutoSlugField


class Category(StatusTimestampBase, ImageBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RecipeDetails(StatusTimestampBase, ImageBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350, blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.title


class RecipeIngredients(TimestampBase):
    recipe = models.ForeignKey(
        RecipeDetails,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )
    title = models.CharField(max_length=150, blank=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.recipe.title} - {self.title}"


class Product(StatusTimestampBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="product_brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=150, blank=True)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    name = models.CharField(max_length=150)
    image_alt = models.CharField(max_length=100, blank=True)
    homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_details", null=True, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="product_details",
        on_delete=models.CASCADE,
    )
    sub_categories = models.CharField(max_length=100, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_code = models.CharField(max_length=100, blank=True, unique=True)
    net_weight = models.CharField(max_length=100, blank=True)
    nutrition = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    storage_instructions = models.TextField(blank=True)
    shelf_life = models.CharField(max_length=150, blank=True)
    how_to_cook = models.TextField(blank=True)
    allergic = models.TextField(blank=True)
    grade = models.CharField(max_length=2000, blank=True)
    origin = models.CharField(max_length=100, blank=True)
    packing = models.CharField(max_length=2000, blank=True)

    def __str__(self) -> str:
        return self.product.name


class RecipeImage(ImageBase, TimestampBase):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
        related_name="recipe_image",
    )

    def __str__(self):
        return self.recipe.title


class Subcategory(StatusTimestampBase):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
