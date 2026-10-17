from django.db import models

# Create your models here.

class Cuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    favourite_cube = models.CharField(max_length=20)
    bio = models.TextField(blank=True, default='This cuber has not added his bio yet')
    date_of_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
