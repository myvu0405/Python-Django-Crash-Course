from django import forms
from django.forms import ModelForm

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields='__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields='__all__'
        widgets = {'post': forms.HiddenInput()}
