from django.shortcuts import render,get_object_or_404,redirect
from .models import Bamboo
from taggit.models import Tag
from django.views.generic import ListView
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import BambooForm,BambooCheckForm


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context



def bamboo_create(request):
    form = BambooForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        instance.user = request.user
        instance.save()
        form.save_m2m()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
            "form":form,

            }
    return render(request,"bamboo/bamboo_form.html",context)

def bamboo_update(request, id=None):
    instance = get_object_or_404(Bamboo, id=id)
    form = BambooForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context ={
            "title":instance.title,
            "instance":instance,
            "form":form,
            }
    return render(request, "bamboo/bamboo_form.html",context)



def bamboo_list(request):

    qs = Bamboo.objects.all().order_by('-timestamp')

    rank_hit = Bamboo.objects.all().order_by('-hit')[:5]
    rank_like = Bamboo.objects.all().order_by('-likes')[:5]
    recent_post = Bamboo.objects.all().order_by('-timestamp')[:10]

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
            "bamboo_list":contacts, 
            "rank_hit":rank_hit,
            "rank_like":rank_like,
            'recent_post':recent_post,
            "title":"대나무숲",
            }
    return render(request,"bamboo/bamboo_list.html",context)


def bamboo_detail(request,id):
    instance = get_object_or_404(Bamboo, id=id) 
    liked = False

    post_id = instance.id

    if request.session.get("has_liked_"+str(post_id), liked):
        liked =True

    instance.hit += 1
    instance.save()

    context = {
            "instance" : instance,
            'liked':liked,
            'title':'대나무숲',
            }
    return render(request, "bamboo/bamboo_detail.html",context)



def bamboo_delete(request, id=None):
    instance = get_object_or_404(Bamboo, id=id)
    instance.delete()
    return redirect("bamboo:bamboo_list")


def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Bamboo.objects.get(id=int(post_id))
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


def bamboo_check(request,id=None):

    password = True
    if request.method == "POST":
        instance = get_object_or_404(Bamboo, id=id)
        form = BambooCheckForm(request.POST)

        if form.is_valid():
            if instance.password == form.cleaned_data['password']:
                return HttpResponseRedirect(instance.get_update_url())
            else:
                password = False


    else:
        form = BambooCheckForm()
            

    print(password)
    return render(request, "bamboo/bamboo_check.html",{"form":form,"password":password})


def bamboo_check_delete(request,id=None):

    password = True
    if request.method == "POST":
        instance = get_object_or_404(Bamboo, id=id)
        form = BambooCheckForm(request.POST)

        if form.is_valid():
            if instance.password == form.cleaned_data['password']:
                return HttpResponseRedirect(instance.get_delete_url())
            else:
                password = False


    else:
        form = BambooCheckForm()
            

    print(password)
    return render(request, "bamboo/bamboo_check_delete.html",{"form":form,"password":password})


class TagIndexView(TagMixin, ListView):
    template_name = 'bamboo/bamboo_tag_list.html'
    model = Bamboo
    context_object_name = 'bamboo_list'

    def get_queryset(self):
        return Bamboo.objects.filter(tags1__slug=self.kwargs.get('slug'))




