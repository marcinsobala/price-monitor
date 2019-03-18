from django import forms
from .models import TrackedPrice

class NewPriceForm(forms.ModelForm):

    class Meta:
        model = TrackedPrice
        fields = ('url', 'when_inform', 'percent_drop', 'desired')

class EditPriceForm(forms.ModelForm):

    class Meta:
        model = TrackedPrice
        fields = ('name', 'when_inform', 'percent_drop', 'desired')