from django.apps import AppConfig


class PrufungConfig(AppConfig):
    """ Функция регистрации приложения (prufung)экзамен """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prufung'
    verbose_name = 'Посты для экзамена'
