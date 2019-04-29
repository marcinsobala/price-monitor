from django import forms
from .models import TrackedPrice

class NewPriceForm(forms.ModelForm):

    class Meta:
        model = TrackedPrice
        fields = ('url', 'when_inform', 'percent_drop', 'desired')
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'https://'})
        }
        labels = {
            'url': 'Adres produktu',
            'when_inform': 'Wyślij powiadomienie',
            'desired': '',
            'percent_drop': ''
        }



class EditPriceForm(forms.ModelForm):

    class Meta:
        model = TrackedPrice
        fields = ('name', 'when_inform', 'percent_drop', 'desired')
        labels = {
            'name': 'Nazwa produktu',
            'when_inform': 'Wyślij powiadomienie',
            'desired': '',
            'percent_drop': ''
        }