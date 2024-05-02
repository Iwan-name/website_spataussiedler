from django import forms

from .models import UnterlagenModel


class UnterlagenForm(forms.ModelForm):
    class Meta:
        model = UnterlagenModel
        fields = ['name', 'beschreibung', 'file']
