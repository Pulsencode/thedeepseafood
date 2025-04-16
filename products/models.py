from django.db import models
from autoslug import AutoSlugField

from company.models import Brand, TimestampBase, StatusTimestampBase


class Category(StatusTimestampBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    name = models.TextField(null=True)
    image = models.FileField(upload_to="category", null=True)

    def __str__(self) -> str:
        return self.name


class Product(TimestampBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        related_name="product_brand",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(null=True)
    type = models.TextField(null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to="product", null=True)
    homepage = models.BooleanField(null=False, blank=True, default=False)
    slug = AutoSlugField(
        populate_from="name",
        editable=True,
        always_update=True,
        null=True,
    )


class RecipeDetails(StatusTimestampBase):
    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title


class RecipeIngredients(TimestampBase):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.recipe.title


class RecipeImage(TimestampBase):
    recipe = models.ForeignKey(
        RecipeDetails,
        null=False,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="recipe_img", null=True)

    def __str__(self) -> str:
        return self.recipe.title


# class ProductDetails(models.Model):
#     product = models.ForeignKey(Product,related_name='product_details',null=True,on_delete=models.CASCADE)
#     category = models.ForeignKey(
#         Category,
#         null=True,
#         blank=True,
#         related_name="product_category",
#         on_delete=models.CASCADE,
#     )
#     sub_categories = models.TextField(null=True)
#     price = models.CharField(max_length=100, null=True, blank=True)
#     product_code = models.CharField(max_length=100, null=True, blank=True)
#     net_weight = models.CharField(max_length=100, null=True, blank=True)
#     description = models.TextField(null=True, blank=True) # used as nutrition facts
#     ingredients = models.TextField(null=True, blank=True)
#     instructions = models.TextField(null=True, blank=True)
#     storage_instructions = models.TextField(null=True, blank=True)
#     shelf_life = models.TextField(null=True, blank=True)
#     how_to_cook = models.TextField(null=True, blank=True)
#     causion = models.TextField(null=True, blank=True) # Caution is used as the allergen Information
#     grade = models.CharField(max_length=2000, null=True, blank=True)
#     origin = models.CharField(max_length=100, null=True, blank=True)
#     packing = models.CharField(max_length=2000, null=True, blank=True)
#     status = models.BooleanField(null=False, blank=True, default=True)

#     def __str__(self) -> str:
#         return self.product.name
