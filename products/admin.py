from django.contrib import admin

# Register your models here.

from products.models import Product,ProductDetails,RecipeDetails,RecipeImage,Category,RecipeIngredients


admin.site.register(ProductDetails)
admin.site.register(Product)
admin.site.register(RecipeDetails)
admin.site.register(RecipeImage)
admin.site.register(Category)
admin.site.register(RecipeIngredients)



