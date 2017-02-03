from django.shortcuts import render

from notice.models import Notice
from bamboo.models import Bamboo
from album.models import Album
from blog.models import Blog

def home(request):

    return render(request, 'home/home.html', {"title1":"공지사항"})


def list_all(request):

    #notice
    notice_qs = Notice.objects.all().order_by('-timestamp')[:5]
    notice_rank_hit = Notice.objects.all().order_by('-hit')[:5]
    notice_rank_like = Notice.objects.all().order_by('-likes')[:5]

    #bamboo
    bamboo_qs = Bamboo.objects.all().order_by('-timestamp')[:5]
    bamboo_rank_hit = Bamboo.objects.all().order_by('-hit')[:5]
    bamboo_rank_like = Bamboo.objects.all().order_by('-likes')[:5]

    #album
    album_qs_1 = Album.objects.all().order_by('-timestamp')[:3]
    album_qs_2 = Album.objects.all().order_by('-timestamp')[3:6]

    #blog
    blog_qs = Blog.objects.all().order_by('-timestamp')[:5]
    blog_rank_hit = Blog.objects.all().order_by('-hit')[:5]
    blog_rank_like = Blog.objects.all().order_by('-likes')[:5]

    context={
            "notice_list":notice_qs, 
            "notice_rank_hit":notice_rank_hit,
            "notice_rank_like":notice_rank_like,

            "bamboo_list":bamboo_qs, 
            "bamboo_rank_hit":bamboo_rank_hit,
            "bamboo_rank_like":bamboo_rank_like,

            "album_list_1":album_qs_1,
            "album_list_2":album_qs_2,

            "blog_list":blog_qs,
            "blog_rank_hit":blog_rank_hit,
            "blog_rank_like":blog_rank_like,

    }
    return render(request,"home/home.html",context)

def rule(request):
    return render(request, 'home/rule.html',{})


def tree(request):
    return render(request, 'home/tree.html',{})
