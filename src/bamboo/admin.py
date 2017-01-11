from django.contrib import admin
from .models import Bamboo
from django_summernote.admin import SummernoteModelAdmin



class BambooModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Bamboo,BambooModelAdmin)




