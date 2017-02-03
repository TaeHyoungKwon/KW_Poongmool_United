from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField


class Blog(models.Model):
    name = models.CharField(max_length=30,default="익명")
    title = models.CharField(max_length=220)
    message = models.TextField(default=None,null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = ImageField(upload_to='photos',null=True,blank=True)
    likes = models.PositiveIntegerField(default=0)
    hit = models.IntegerField(default=0)
    password = models.CharField(max_length=10)
    tags = TaggableManager()



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail",kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("blog:blog_update",kwargs={"id": self.id})

    def get_check_url(self):
        return reverse("blog:blog_check",kwargs={"id":self.id})

    def get_check_delete_url(self):
        return reverse("blog:blog_check_delete",kwargs={"id":self.id})
    def get_delete_url(self):
        return reverse("blog:blog_delete",kwargs={"id":self.id})
    @property
    def total_likes(self):
        return self.likes.count()


    @property

    def thumb_url(self):
        thumb = get_thumbnail(self.photo, '100x100',crop='center', quality=70)
        return thumb.url

    def as_dict(self):
        return {
                'id':self.id,
                'author':'anonymous',
                'message':self.message,
                'is_public':True,
                'photos':[
                    {'url':self.photo.url, 'thumb_url':self.thumb_url},
                    ],
                
                
                }


