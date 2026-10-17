from django import forms
from .models import Cuber

class CuberForm(forms.ModelForm):

    class Meta:
        model = Cuber
        fields = ['first_name', 'last_name', 'country', 'favourite_cube', 'bio']