from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UmzugModels(models.Model):
    """ Модель для создания постов про переезд """
    name = models.CharField(max_length=200)
    beschreibung = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='umzug'
    )
    file = models.FileField(upload_to='Umzug/')

    class Meta:
        verbose_name = 'Посты про переезд'
