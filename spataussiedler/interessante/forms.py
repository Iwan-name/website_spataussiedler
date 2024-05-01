from django import forms

from .models import InteressanteOrte


class InteressanteHinzufugenForm(forms.ModelForm):
    class Meta:
        model = InteressanteOrte
        fields = ('name', 'ortung', 'beschreibung', 'bild')
