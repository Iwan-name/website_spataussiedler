from django.contrib import admin

from interessante.models import InteressanteOrte
from prufung.models import PrufungModels
from unterlagen.models import UnterlagenModel
from umzug.models import UmzugModels

# Регистрация моделей в Админке

admin.site.register(InteressanteOrte)
admin.site.register(PrufungModels)
admin.site.register(UnterlagenModel)
admin.site.register(UmzugModels)
