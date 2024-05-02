from django import forms
from .models import PrufungModels


class PrufungForm(forms.ModelForm):
    class Meta:
        model = PrufungModels
        fields = ['name', 'beschreibung', 'file']
