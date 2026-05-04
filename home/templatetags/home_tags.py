from django import template
from home.models import HomePage

register = template.Library()

@register.simple_tag
def get_home_page_data():
    return HomePage.objects.live().first()