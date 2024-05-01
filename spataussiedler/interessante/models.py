from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class InteressanteOrte(models.Model):
    name = models.CharField(max_length=100)
    ortung = models.CharField(max_length=150)
    beschreibung = models.TextField()
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='interessanteOrte'
    )
    bild = models.ImageField(upload_to='interessanteOrte/')
