from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields
from .models import Bamboo


class BambooForm(forms.ModelForm):
    message = fields.SummernoteTextFormField()
    class Meta:
        model = Bamboo
        fields = [
                "title",
                "password",
                'message',
                'tags1',
                
                ]
        widgets = {
                "foo":  SummernoteWidget(),
                
                }

class BambooCheckForm(forms.Form):
    password = forms.CharField(max_length=10)
