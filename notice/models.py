from django.db import models


class Notice(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=220)
    message = models.TextField(default=None)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




