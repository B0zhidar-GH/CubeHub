from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.

class Cube(models.Model):

    class CubeChoices(models.TextChoices):

        #Regular cubes
        CUBE_2X2 = '222', '2x2x2 Cube'
        CUBE_3X3 = '333', '3x3x3 Cube'
        CUBE_4X4 = '444', '4x4x4 Cube'
        CUBE_5X5 = '555', '5x5x5 Cube'
        CUBE_6X6 = '666', '6x6x6 Cube'
        CUBE_7X7 = '777', '7x7x7 Cube'

        #Irregular cubes
        CLOCK = 'clock', 'Clock'
        MEGAMINX = 'minx', 'Megaminx'
        PYRAMINX = 'pyram', 'Pyraminx'
        SKWEB = 'skewb', 'Skewb'

    class CategoryEvent(models.TextChoices):

        # Standard NxN Events
        CUBE_2X2 = '222', '2x2x2 Cube'
        CUBE_3X3 = '333', '3x3x3 Cube'
        CUBE_4X4 = '444', '4x4x4 Cube'
        CUBE_5X5 = '555', '5x5x5 Cube'
        CUBE_6X6 = '666', '6x6x6 Cube'
        CUBE_7X7 = '777', '7x7x7 Cube'

        # Blindfolded Events
        BLD_3X3 = '333bf', '3x3x3 Blindfolded'
        BLD_4X4 = '444bf', '4x4x4 Blindfolded'
        BLD_5X5 = '555bf', '5x5x5 Blindfolded'
        MULTI_BLD = '333mbf', '3x3x3 Multi-Blind'

        # Variant / Specialty Events
        OH_3X3 = '333oh', '3x3x3 One-Handed'
        FMC_3X3 = '333fm', '3x3x3 Fewest Moves'

        # Non-NxN Shape Puzzles
        CLOCK = 'clock', 'Clock'
        MEGAMINX = 'megam', 'Megaminx'
        PYRAMINX = 'pyram', 'Pyraminx'
        SKWEB = 'skewb', 'Skewb'
        SQ1 = 'sq1', 'Square-1'

    cube = models.CharField(max_length=20, choices=CubeChoices.choices)
    category_event = models.CharField(max_length=20, choices=CategoryEvent.choices)
    brand = models.CharField(max_length=20, validators = [
        MaxLengthValidator(limit_value=20,
                           message='This field cannot be longer than 20 characters')
    ])
    date_of_registration = models.DateTimeField(auto_now_add=True)

    owners = models.ManyToManyField('cubers.Cuber', related_name='cubes')

    def __str__(self):
        return (
            f'{self.get_cube_display()} - '
            f'{self.get_category_event_display()} - '
            f'{self.brand}'
        )