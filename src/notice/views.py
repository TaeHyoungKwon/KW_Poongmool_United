from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView

from .models import Notice

from taggit.models import Tag



def notice_list(request):

    qs = Notice.objects.all().order_by('-timestamp')

    rank_hit = Notice.objects.all().order_by('-hit')[:5]
    rank_like = Notice.objects.all().order_by('-likes')[:5]

    query = request.GET.get("q")
    if query:
        qs = qs.filter(
                
                Q(title__icontains=query)|
                Q(message__icontains=query)
                ).distinct()

    paginator = Paginator(qs, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context={
            "notice_list":contacts, 
            "rank_hit":rank_hit,
            "rank_like":rank_like,
            "title":"공지사항",
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

    title = "공지사항"

    context = {
            "instance" : instance,
            'liked':liked,
            'title':"공지사항",
    }
    return render(request, "notice/notice_detail.html",context)



def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        print(post_id)
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





class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagIndexView(TagMixin, ListView):
    template_name = 'notice/notice_tag_list.html'
    model = Notice
    context_object_name = 'notice_list'

    def get_queryset(self):
        return Notice.objects.filter(tags__slug=self.kwargs.get('slug'))


