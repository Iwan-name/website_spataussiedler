from django.apps import AppConfig


class InteressanteConfig(AppConfig):
    """ Функция регистрации приложения (interessante)Интересные места """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interessante'
    verbose_name = 'Интересные места'
