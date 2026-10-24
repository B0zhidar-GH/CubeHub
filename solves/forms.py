from django import forms
from .models import Solve

class SolveForm(forms.ModelForm):

    registration_date = forms.DateTimeField(
        label='Date of registration:',
        required=False,
        disabled=True
    )

    class Meta:
        model = Solve
        fields = ['time', 'cube', 'cuber', 'scramble']

        labels = {
            'time': 'Enter the time in seconds:',
            'cube': 'Select the cube:',
            'cuber': 'Select the cuber:',
            'scramble': 'Enter the scramble',
        }

        widgets = {
            'time': forms.NumberInput(
                attrs={
                    'placeholder': 'eg. 9.45',
                    'oninvalid': "this.setCustomValidity('Time cannot be empty or have white spaces!')",
                    "oninput": 'this.setCustomValidity("")',
                    'step': '0.01',
                }
            ),

            'cube': forms.Select(
                attrs={
                    #'placeholder': 'eg. 9.45',
                    'oninvalid': "this.setCustomValidity('Please, complete this field!')",
                    "oninput": 'this.setCustomValidity("")'
                }
            ),

            'cuber': forms.Select(
                attrs={
                    # 'placeholder': 'eg. 9.45',
                    'oninvalid': "this.setCustomValidity('Please, complete this field!')",
                    "oninput": 'this.setCustomValidity("")'
                }
            ),

            'scramble': forms.TextInput(
                attrs={
                    'placeholder': "eg. R2 D' F B L2 U'...",
                    'oninvalid': "this.setCustomValidity('Scramble cannot be empty or have white spaces!')",
                    "oninput": 'this.setCustomValidity("")'
                }
            ),
        }

        error_messages = {
            'time': {
                'required': 'Time cannot be empty or have white spaces!'
            },

            'cube': {
                'required': 'Please, complete this field!'
            },

            'cuber': {
                'required': 'Please, complete this field!'
            },

            'scramble': {
                'required': 'Scramble cannot be empty or have white spaces!!'
            },
        }

    def clean_time(self):
        value = self.cleaned_data.get('time', '')

        if value is not None and value <= 0:
            raise forms.ValidationError(
                'Time must be a positive number!'
            )

        return value

    def clean_scramble(self):
        value = self.cleaned_data.get('scramble', '').strip()

        if not value:
            raise forms.ValidationError(
                'Scramble cannot be empty or have white spaces!'
            )

        return value

