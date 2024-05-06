from django import forms

from unterlagen.models import UnterlagenModel
from prufung.models import PrufungModels


class UnterlagenForm(forms.ModelForm):
    """ Форма для создания поста про документы """
    class Meta:
        model = UnterlagenModel
        fields = ['name', 'beschreibung', 'file']


class PrufungForm(forms.ModelForm):
    """ Форма для создания поста про экзамен """
    class Meta:
        model = PrufungModels
        fields = ['name', 'beschreibung', 'file']
