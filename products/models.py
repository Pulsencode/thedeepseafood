from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

from company.models import Brand, ImageBase, StatusTimestampBase


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

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(StatusTimestampBase, ImageBase):
    TYPE_CHOICES = (
        ("", "Select the Type"),
        ("local catch", "Local Catch"),
        ("imported", "Imported"),
        ("value added", "Value Added"),
    )
    name = models.CharField(max_length=150)
    homepage = models.BooleanField(default=False)
    sequence = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    slug = AutoSlugField(
        populate_from="product__name",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.name


class Subcategory(StatusTimestampBase):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return str(self.name)


class ProductDetails(StatusTimestampBase):
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
    sub_categories = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
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
    slug = AutoSlugField(
        populate_from="name",
        editable=True,
        always_update=True,
        null=True,
        blank=True,
        unique=True,
        max_length=100,
    )

    def name(self):
        return self.product.name if self.product else ""

    def __str__(self) -> str:
        return self.product.name

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"
