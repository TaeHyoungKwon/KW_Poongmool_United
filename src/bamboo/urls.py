from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.bamboo_list, name='bamboo_list'),
        url(r'^(?P<id>\d+)/$', views.bamboo_detail, name='bamboo_detail'),
        url(r'^create/$', views.bamboo_create, name='bamboo_create'),
        url(r'^(?P<id>\d+)/update/$', views.bamboo_update, name='bamboo_update'),
        url(r'^(?P<id>\d+)/check/$', views.bamboo_check, name='bamboo_check'),
        url(r'^(?P<id>\d+)/check_delete/$', views.bamboo_check_delete, name='bamboo_check_delete'),

        url(r'^(?P<id>\d+)/delete/$', views.bamboo_delete, name='bamboo_delete'),
        url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
        url(r'^tag/(?P<slug>[-\w]+)/', views.TagIndexView.as_view(), name='tagged'),

        ]
