from django.shortcuts import render,get_object_or_404
from .models import Notice
from django.views.generic import ListView


def notice_list(request):

    qs = Notice.objects.all().order_by('-timestamp')
    context={
            "notice_list":qs, 
    }
    return render(request,"notice/notice_list.html",context)


def notice_detail(request,id=None):
    instance = get_object_or_404(Notice, id=id) 
    context = {
            "instance" : instance,
    }
    return render(request, "notice/notice_detail.html",context)
