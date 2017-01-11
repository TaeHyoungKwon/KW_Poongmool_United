from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields
from .models import Blog


class BlogForm(forms.ModelForm):
    message = fields.SummernoteTextFormField(label=('내용'))
    class Meta:
        model = Blog
        fields = [
                "name",
                "title",
                "password",
                'message',
                'photo',
                'tags',
                
                
                ]
        widgets = {
                "foo":  SummernoteWidget(),
                
                }
        labels ={
                "name":('작성자'),
                "title":('제목'),
                "password":('패스워드'),
                'photo':('대표 이미지 or 프로필 사진'),
                'tags':('태그'),

                
                }

class BlogCheckForm(forms.Form):
    password = forms.CharField(max_length=10)
