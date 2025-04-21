from django.db import models
from django.utils.text import slugify
from company.models import Brand


class Category(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="categoryimg", blank=True)

    status = models.BooleanField(default=True)
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
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=350, blank=True, null=True)
    image = models.ImageField(upload_to="recipeimg")
    image_alt = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(
        RecipeDetails,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )
    title = models.CharField(max_length=150, blank=True)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.recipe.title} - {self.title}"


class Product(models.Model):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="product_brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=150, blank=True)
    slug_product = models.SlugField(
        max_length=250, unique=True, blank=True, editable=False
    )
    name = models.CharField(max_length=150)
    image_alt = models.CharField(max_length=100, blank=True)
    homepage = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug_product or self.title_changed():
            self.slug_product = slugify(self.name)
        super().save(*args, **kwargs)

    def title_changed(self):
        if self.id:
            return self.name != Product.objects.get(pk=self.id).name
        return False

    def __str__(self) -> str:
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
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
