from django import forms
from .models import Cube

class CubeForm(forms.ModelForm):

    registration_date = forms.DateTimeField(
        label='Date of registration:',
        required=False,
        disabled=True
    )

    class Meta:
        model = Cube
        fields = ['cube', 'category_event', 'brand', 'owners']

        labels = {
            'cube': "Select your cube's type:",
            'category_event': "Select your cube's event:",
            'brand': "Enter your cube's brand:",
            'owners': "Enter your cube's owner",
        }

        widgets = {
            'cube': forms.Select(
                attrs={
                    'oninvalid': "this.setCustomValidity('Please, complete this field!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'category_event': forms.Select(
                attrs={
                    'oninvalid': "this.setCustomValidity('Please, complete this field!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'eg. MoYo',
                    'oninvalid': "this.setCustomValidity('Brand cannot be empty or have white spaces!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'owners': forms.SelectMultiple(
                attrs={
                    'oninvalid': "this.setCustomValidity('Please, complete this field!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),
        }

        error_messages = {
            'cube': {
                'required': 'Please, complete this field!'
            },

            'category_event': {
                'required': 'Please, complete this field!'
            },

            'brand': {
                'required': 'Brand cannot be empty or have white spaces!'
            },

            'owners': {
                'required': 'Please, complete this field!'
            },
        }

    def clean_brand(self):
        value = self.cleaned_data.get('brand', '').strip()
        if not value:
            raise forms.ValidationError(
                'Brand cannot be empty or have white spaces!'
            )
        return value
