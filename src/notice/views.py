from django.shortcuts import render,get_object_or_404,redirect
from .models import Notice
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from .forms import NoticeForm



def notice_create(request):
    form = NoticeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        print(form.cleaned_data.get("title"))
        instance.save()

    context = {
            "form":form,
            
            }
    return render(request,"notice/notice_form.html",context)


def notice_list(request):

    qs = Notice.objects.all().order_by('-timestamp')
    context={
            "notice_list":qs, 
    }
    return render(request,"notice/notice_list.html",context)


def notice_detail(request,id):
    instance = get_object_or_404(Notice, id=id) 
    context = {
            "instance" : instance,
    }
    return render(request, "notice/notice_detail.html",context)



def notice_update(request, id=None):
    instance = get_object_or_404(Notice, id=id)
    form = NoticeForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context ={
            "title":instance.title,
            "instance":instance,
            "form":form,
    }
    return render(request, "notice/notice_form.html",context)


def notice_delete(request, id=None):
    instance = get_object_or_404(Notice, id=id)
    instance.delete()
    return redirect("notice:notice_list")

