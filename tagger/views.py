from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tag, TaggedItem
from .forms import TagItForm
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect


def tag_cloud(request):
    tags = Tag.objects.all()
    tag_list = []
    for tag in tags:
        tag_list.append((tag.tag, len(tag.tagged_items.all())))
    context_dict = {'tag_list': tag_list}
    return render(request, 'tagger/tag_cloud.html', context_dict)

@login_required
def tag_it(request, model, model_id):
    user = request.user
    content_type = ContentType.objects.get(model=model)

    if request.method == 'POST':
        if request.POST.get('tag_new'):
            tag = Tag(tag=request.POST.get('tag_new', None), created_by=user)
            tag.save()
            tagget_item = TaggedItem(content_type=content_type, object_id=model_id)
            tagget_item.created_by = user
            tagget_item.tag = tag
            tagget_item.save()
        elif request.POST.get('tag', None):
            tag = Tag.objects.get(id=request.POST.get('tag', None))
            tagget_item = TaggedItem(content_type=content_type, object_id=model_id)
            tagget_item.created_by = user
            tagget_item.tag = tag
            tagget_item.save()

    form = TagItForm()
    tags = TaggedItem.objects.filter(content_type=content_type, object_id=model_id)
    form.fields["tag"].queryset = Tag.objects.exclude(tag__in=[o.tag for o in tags])

    context_dict = {'form': form, 'tags': tags}
    return render(request, 'tagger/tag_it.html', context_dict)

@login_required
def tag_del(request, id):
    tagged_item = TaggedItem.objects.get(id=id)
    find_all_tagged_items = TaggedItem.objects.filter(tag=tagged_item.tag)
    if find_all_tagged_items.count() == 1:
        tag = Tag.objects.get(id=tagged_item.tag_id)
        tag.delete()
    else:
        tagged_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
