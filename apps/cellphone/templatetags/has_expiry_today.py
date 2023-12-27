from django import template

register = template.Library()


@register.filter
def has_expiry_today(objects):
    return any(obj.expires_today for obj in objects)
