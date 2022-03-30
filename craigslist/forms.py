from django import forms
from django.forms import ModelForm

from .models import *

class ListingForm(forms.ModelForm):

    class Meta:
        model=Listing
        fields=['title', 'description','price','location','contact']

