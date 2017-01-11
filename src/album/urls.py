from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.album_list, name='album_list'),
        url(r'^(?P<id>\d+)/$', views.album_detail, name='album_detail'),
        url(r'^create/$', views.album_create, name='album_create'),
        url(r'^(?P<id>\d+)/update/$', views.album_update, name='album_update'),
        url(r'^(?P<id>\d+)/check/$', views.album_check, name='album_check'),
        url(r'^(?P<id>\d+)/check_delete/$', views.album_check_delete, name='album_check_delete'),

        url(r'^(?P<id>\d+)/delete/$', views.album_delete, name='album_delete'),
        url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
        url(r'^tag/(?P<slug>[-\w]+)/', views.TagIndexView.as_view(), name='tagged'),

        ] 
