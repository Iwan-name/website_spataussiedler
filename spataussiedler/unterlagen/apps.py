from django.apps import AppConfig


class UnterlagenConfig(AppConfig):
    """ Функция регистрации приложения (unterlagen)Документы """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unterlagen'
    verbose_name = 'Посты для документов'
