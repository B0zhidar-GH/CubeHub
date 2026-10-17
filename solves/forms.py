from django import forms
from .models import Solve

class SolveForm(forms.ModelForm):

    class Meta:
        model = Solve
        fields = ['time', 'cube', 'cuber', 'scramble']