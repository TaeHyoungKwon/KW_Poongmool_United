from django.contrib import admin
from .models import Notice
from django_summernote.admin import SummernoteModelAdmin



class NoticeModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Notice,NoticeModelAdmin)

