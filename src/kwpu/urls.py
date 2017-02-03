"""kwpu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
import notice,bamboo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notice/', include('notice.urls',namespace='notice')),
    url(r'^bamboo/', include('bamboo.urls',namespace='bamboo')),
    url(r'^album/', include('album.urls',namespace='album')),
    url(r'^blog/', include('blog.urls',namespace='blog')),



    url(r'^home/', include('home.urls',namespace='home')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^notice/like-blog/$', notice.views.like_count_blog, name='like_count_blog'),
    url(r'^bamboo/like-blog/$', bamboo.views.like_count_blog, name='like_count_blog'),
  
    url(r'^calendar/', include('happenings.urls', namespace='calendar')),

    url(r'^$' , lambda r: redirect('home:home')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
