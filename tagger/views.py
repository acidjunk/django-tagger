from django.shortcuts import render

# Create your views here.
from .models import Tag, TaggedItem

def tag_cloud(request):
    tags=Tag.objects.all()
    tag_list=[]
    for tag in tags:
        tag_list.append((tag.tag, len(tag.tagged_items.all())))
    context_dict = { 'tag_list': tag_list }
    return render(request, 'tagger/tag_cloud.html', context_dict)