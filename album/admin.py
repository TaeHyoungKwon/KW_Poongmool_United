from django.contrib import admin
from .models import Album
from django_summernote.admin import SummernoteModelAdmin



class AlbumModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Album,AlbumModelAdmin)




