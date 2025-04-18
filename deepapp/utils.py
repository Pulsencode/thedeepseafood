from django.utils.text import slugify
import uuid


def generate_slug(name:str)->str:
    from .models import Product
    name = slugify(name)
    while(Product.objects.filter(slug_product=name).exists()):
        name = f'{slugify(name)}-{str(uuid.uuid4())[:4]}'
    return name