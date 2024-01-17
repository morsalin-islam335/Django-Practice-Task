from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    instrument_type = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.first_name + " "+ self.last_name}'




class Album(models.Model):
    album_name = models.CharField(max_length = 50)
    musician = models.ForeignKey(Musician, on_delete= models.CASCADE, related_name = "albums")
    album_release_date = models.DateField()
    choice = [
        (1,"*"),
        (2,"**"),
        (3,'***'),
        (4,'****'),
        (5,'*****')
    ]
    rating = models.IntegerField(choices = choice)

    def __str__(self):
        return self.album_name
