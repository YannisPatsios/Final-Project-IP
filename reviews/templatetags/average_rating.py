from django import template

register = template.Library()

@register.filter
def average_rating(queryset):
    values = [getattr(obj, 'rating', 0) for obj in queryset if getattr(obj, 'rating', None) is not None]
    if not values:
        return 0
    return sum(values) / len(values) 