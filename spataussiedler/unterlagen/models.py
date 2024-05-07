from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UnterlagenModel(models.Model):
    """ Модель для создания постов про документы """
    name = models.CharField(max_length=200)
    beschreibung = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='unterlagen'
    )
    file = models.FileField(upload_to='Unterlagen/')

    class Meta:
        verbose_name = 'Посты про документы'
