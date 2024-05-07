from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """ Функция регистрации приложения (user_profile)Профиль пользователя """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
    verbose_name = 'Профиль пользователя'
