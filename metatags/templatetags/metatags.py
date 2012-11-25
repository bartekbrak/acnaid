from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('templatetags/metatags/meta_tags_dev.html', takes_context=True)
def meta_tags(context):
    context.update({
        'tags': MetaTag.objects.all(),
    })
    return context

