from models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post_adv', 'src', 'description']
