from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.notice_list, name='notice_list'),
        #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
                ]
