from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^tag-cloud$', views.tag_cloud, name='tag-cloud'),
)