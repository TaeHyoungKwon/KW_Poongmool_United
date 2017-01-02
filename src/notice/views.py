from django.shortcuts import render,get_object_or_404,redirect
from .models import Notice
from django.views.generic import ListView
from django.http import HttpResponseRedirect,HttpResponse

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

    rank_hit = Notice.objects.all().order_by('-hit')[:5]
    rank_like = Notice.objects.all().order_by('-likes')[:5]

    context={
            "notice_list":qs, 
            "rank_hit":rank_hit,
            "rank_like":rank_like,
    }
    return render(request,"notice/notice_list.html",context)


def notice_detail(request,id):
    instance = get_object_or_404(Notice, id=id) 
    liked = False

    post_id = instance.id

    if request.session.get("has_liked_"+str(post_id), liked):
        liked =True

    instance.hit += 1
    instance.save()

    context = {
            "instance" : instance,
            'liked':liked,
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


def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Notice.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            request.session['has_liked_'+post_id] = True
            likes = post.likes + 1
    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)
