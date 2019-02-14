from django import forms
from .models import TrackedPrice

class PriceForm(forms.ModelForm):

    class Meta:
        model = TrackedPrice
        fields = ('url', 'desired')