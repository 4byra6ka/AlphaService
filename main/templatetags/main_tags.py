from datetime import datetime

from django import template

from main.models import Service

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)


@register.filter(name='query_service')
def query_service(value, category):
    services = Service.objects.filter(category=category, archived=False)
    return services
