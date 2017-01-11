from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin



class BlogModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Blog,BlogModelAdmin)
