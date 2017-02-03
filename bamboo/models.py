from django.db import models
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

class Bamboo(models.Model):
    title = models.CharField(max_length=220)
    message = models.TextField(default=None,null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    hit = models.IntegerField(default=0)
    password = models.CharField(max_length=10)
    tags = TaggableManager()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bamboo:bamboo_detail",kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("bamboo:bamboo_update",kwargs={"id": self.id})

    def get_check_url(self):
        return reverse("bamboo:bamboo_check",kwargs={"id":self.id})

    def get_check_delete_url(self):
        return reverse("bamboo:bamboo_check_delete",kwargs={"id":self.id})
    def get_delete_url(self):
        return reverse("bamboo:bamboo_delete",kwargs={"id":self.id})

    def get_tag_list_url(self):
        return reverse("bamboo:tagged",kwargs={"slug":self.tags})

    @property
    def total_likes(self):
        return self.likes.count()

