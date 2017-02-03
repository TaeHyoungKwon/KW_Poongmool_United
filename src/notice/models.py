from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class Notice(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=220)
    message = models.TextField(default=None)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    hit = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notice:notice_detail",kwargs={"id": self.id})

    @property
    def total_likes(self):
        return self.likes.count()




