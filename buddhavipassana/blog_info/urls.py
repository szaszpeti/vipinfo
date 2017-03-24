from django.conf.urls import url
from . import views

app_name = 'blog_info'

urlpatterns = [
    #/blog_info
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<category_id>[0-9]+)/$', views.details, name='blog_details'),
    url(r'^(?P<category_id>[0-9]+)/$', views.read, name='blog_read'),
    url(r'^(?P<category_id>[0-9]+)/like/$', views.like, name='blog_like'),
    url(r'^(?P<category_id>[0-9]+)/dislike/$', views.dislike, name='blog_dislike'),
    url(r'^(?P<category_id>[0-9]+)/delete/$', views.delete, name='blog_delete'),
    url(r'^(?P<category_id>[0-9]+)/read/$', views.read, name='blog_read'),
    # url(r'^(?P<category_id>[0-9]+)/update/$', views.update, name='blog_update'),
    url(r'^create/$', views.blog_create, name='blog_create'),
    # url(r'^blog_new_document/$', views.blog_new_document, name='blog_new_document'),
]
