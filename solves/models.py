from django.db import models
from cubers.models import Cuber
from cubes.models import Cube


# Create your models here.

class Solve(models.Model):
    cuber = models.ForeignKey('cubers.Cuber', on_delete=models.CASCADE, related_name='solves')
    cube = models.ForeignKey(Cube, on_delete=models.CASCADE)
    time = models.DecimalField(max_digits=6, decimal_places=2)
    scramble = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cuber} - {self.time}'