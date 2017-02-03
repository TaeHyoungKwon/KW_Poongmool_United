from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.blog_list, name='blog_list'),
        url(r'^(?P<id>\d+)/$', views.blog_detail, name='blog_detail'),
        url(r'^create/$', views.blog_create, name='blog_create'),
        url(r'^(?P<id>\d+)/update/$', views.blog_update, name='blog_update'),
        url(r'^(?P<id>\d+)/check/$', views.blog_check, name='blog_check'),
        url(r'^(?P<id>\d+)/check_delete/$', views.blog_check_delete, name='blog_check_delete'),

        url(r'^(?P<id>\d+)/delete/$', views.blog_delete, name='blog_delete'),
        url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
        url(r'^tag/(?P<slug>[-\w]+)/', views.TagIndexView.as_view(), name='tagged'),

        ] 
