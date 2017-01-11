from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields
from .models import Album


class AlbumForm(forms.ModelForm):
    message = fields.SummernoteTextFormField(label=('내용'))
    class Meta:
        model = Album
        fields = [
                "name",
                "title",
                "password",
                'message',
                'photo',
                
                
                ]
        widgets = {
                "foo":  SummernoteWidget(),
                
                }
        labels ={
                "name":('작성자'),
                "title":('제목'),
                "password":('패스워드'),
                'photo':('대표 이미지'),

                
                }

class AlbumCheckForm(forms.Form):
    password = forms.CharField(max_length=10)
