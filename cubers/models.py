#from email import message

#from django.core import validators
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.

class Cuber(models.Model):
    first_name = models.CharField(max_length=100, validators = [
        MaxLengthValidator(limit_value=100,
                           message='This field cannot be longer than 100 characters')
    ])

    last_name = models.CharField(max_length=100, validators = [
        MaxLengthValidator(limit_value=100,
                           message='This field cannot be longer than 100 characters')
    ])

    country = models.CharField(max_length=30, validators = [
        MaxLengthValidator(limit_value=30,
                           message='This field cannot be longer than 30 characters')
    ])

    favourite_cube = models.CharField(max_length=20, validators = [
        MaxLengthValidator(limit_value=20,
                           message='This field cannot be longer than 20 characters')
    ])

    bio = models.TextField(blank=True, default='This cuber has not added his bio yet')
    date_of_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
