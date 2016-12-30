from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.notice_list, name='notice_list'),
        url(r'^(?P<id>\d+)/$', views.notice_detail, name='notice_detail'),
                ]
