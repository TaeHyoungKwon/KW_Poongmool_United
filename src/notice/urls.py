from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.notice_list, name='notice_list'),
        url(r'^(?P<id>\d+)/$', views.notice_detail, name='notice_detail'),
        url(r'^create/$', views.notice_create, name='notice_create'),
        url(r'^(?P<id>\d+)/update/$', views.notice_update, name='notice_update'),
        url(r'^(?P<id>\d+)/delete/$', views.notice_delete, name='notice_delete'),


                ]
