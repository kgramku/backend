from django import forms
from .models import Post
from django.conf import settings

MAX_POST_LENGTH = settings.MAX_POST_LENGTH

class Postform(forms.ModelForm):
     class Meta:
         model = Post
         fields = ['content']

     def clean_content(self):
         print('hi')
         content = self.cleaned_data.get('content')
         if len(content) > MAX_POST_LENGTH:
             raise forms.ValidationError("post too long")
         else:
             return content
