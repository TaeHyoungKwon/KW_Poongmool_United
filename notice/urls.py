from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.notice_list, name='notice_list'),
        url(r'^(?P<id>\d+)/$', views.notice_detail, name='notice_detail'),
        url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
        url(r'^tag/(?P<slug>[-\w]+)/', views.TagIndexView.as_view(), name='tagged'),
        
        ]
