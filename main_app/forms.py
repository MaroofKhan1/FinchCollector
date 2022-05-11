from dataclasses import field
from pyexpat import model
from statistics import mode
from django import forms
from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
