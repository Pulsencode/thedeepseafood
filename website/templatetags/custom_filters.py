from django import template

from deepapp.models import Product

register = template.Library()


@register.filter
def get_for_index(list, index):
    return list[index]


@register.filter(name="truncate_chars")
def truncate_chars(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value


@register.filter
def split_by_comma(value):
    if value:
        return value.split(",")
    else:
        return []


@register.filter(name="product_belongs_to_category")
def product_belongs_to_category_filter(product_id, category_id):
    try:
        product = Product.objects.get(id=product_id)
        return product.product_details.filter(
            status=True, category_id=category_id
        ).exists()
    except Product.DoesNotExist:
        return False
