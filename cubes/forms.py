from django import forms
from .models import Cube

class CubeForm(forms.ModelForm):

    class Meta:
        model = Cube
        fields = ['cube', 'category_event', 'brand', 'owners']