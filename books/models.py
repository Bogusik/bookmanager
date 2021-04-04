from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(
        User,
        related_name='books',
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    poster_image = models.ImageField(blank=True, null=True)
