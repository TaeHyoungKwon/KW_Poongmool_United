from django.db import models
from django.core.urlresolvers import reverse

class Notice(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=220)
    message = models.TextField(default=None)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return "/notice/%s" % (self.id)
        return reverse("notice:notice_detail",kwargs={"id": self.id})



