from django import template
from ..models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType

register = template.Library()

def show_tags(model, pk):
    object_type = ContentType.objects.get(model=model)
    tagged_items=TaggedItem.objects.filter(content_type=object_type.id, object_id=pk)
    print tagged_items
    return {'tagged_items': tagged_items, 'model': model, 'pk': pk}

register.inclusion_tag('tagger/templatetags/show_tags.html')(show_tags)
