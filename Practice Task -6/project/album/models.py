from django.db import models

# Create your models here.
from musician.models import Musician
from musician.models import Musician
class Album(models.Model):
    album_name = models.CharField(max_length = 60, verbose_name = 'Album Name')
    musician = models.ForeignKey(Musician, on_delete = models.CASCADE, related_name = 'albums')
    album_release_date = models.DateField()
    choice = [
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****'),
    ]

    rating = models.CharField(max_length =10, choices = choice, verbose_name = "Rating")
