from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 50 , verbose_name = 'Last Name')
    email = models.EmailField(verbose_name = 'Email Address')
    phone_number = models.CharField(max_length = 14, verbose_name = 'Phone Number')
    instrument_type = models.CharField(max_length = 40, verbose_name = 'Instrument Type')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
