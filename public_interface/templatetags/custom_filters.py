from django import template
from products.models import Product

# This makes a new library of custom template filters
register = template.Library()


@register.filter
def get_for_index(list, index):
    """
    Template filter to get an element at a specific index from a list.
    Example in template: {{ mylist|get_for_index:2 }}
    """
    return list[index]


@register.filter(name="truncate_chars")
def truncate_chars(value, max_length):
    """
    Template filter to truncate a string to 'max_length' characters,
    and add '...' if the text was longer.
    Example in template: {{ mystring|truncate_chars:20 }}
    """
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value


@register.filter
def split_by_comma(value):
    """
    Template filter to split a string by commas and return a list.
    If the value is empty, returns an empty list.
    Example in template: {{ csv_string|split_by_comma }}
    """
    if value:
        return value.split(",")
    else:
        return []


@register.filter(name="product_belongs_to_category")
def product_belongs_to_category_filter(product_id, category_id):
    """
    Template filter to check if a product (by its ID) belongs to a specific category (by its ID).
    It checks the product's related 'product_details' for a matching active (status=True) category.
    Returns True or False.
    Example in template: {% if product.id|product_belongs_to_category:category.id %}
    """
    try:
        # Get the product object by ID
        product = Product.objects.get(id=product_id)
        # Check if it has any active product_details in the given category
        return product.product_details.filter(
            status=True, category_id=category_id
        ).exists()
    except Product.DoesNotExist:
        return False
