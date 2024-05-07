from django import forms
from interessante.models import InteressanteOrte
from prufung.models import PrufungModels
from umzug.models import UmzugModels
from unterlagen.models import UnterlagenModel


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


class UmzugForm(forms.ModelForm):
    """ Форма для создания поста про переезд """

    class Meta:
        model = UmzugModels
        fields = ['name', 'beschreibung', 'file']


class InteressanteHinzufugenForm(forms.ModelForm):
    """ Форма для создания поста про интересные места """

    class Meta:
        model = InteressanteOrte
        fields = ('name', 'ortung', 'beschreibung', 'bild')
