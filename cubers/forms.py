from django import forms
from .models import Cuber

class CuberForm(forms.ModelForm):

    registration_date = forms.DateTimeField(
        label='Date of registration:',
        required=False,
        disabled=True
    )

    class Meta:
        model = Cuber
        fields = ['first_name', 'last_name', 'country', 'favourite_cube', 'bio']



        labels = {
            'first_name': 'Enter your first name:',
            'last_name': 'Enter your last name:',
            'country': 'Enter your country:',
            'favourite_cube': 'Enter your favourite cube:',
            'bio': 'Enter your bio(not required):',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'eg. Alex',
                    'oninvalid': "this.setCustomValidity('First name cannot be empty or have white spaces!')",
                    "oninput": 'this.setCustomValidity("")'}
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'eg. Ivanov',
                    'oninvalid': "this.setCustomValidity('Last name cannot be empty or have white spaces!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'country': forms.TextInput(
                attrs={
                    'placeholder': 'eg. USA',
                    'oninvalid': "this.setCustomValidity('Country cannot be empty or have white spaces!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'favourite_cube': forms.TextInput(
                attrs={
                    'placeholder': 'eg. 3x3',
                    'oninvalid': "this.setCustomValidity('Favourite cube name cannot be empty or have white spaces!')",
                    'oninput': "this.setCustomValidity('')",
                }
            ),

            'bio': forms.Textarea(attrs={}),
        }


        error_messages = {
            'first_name': {
                'required': 'First name cannot be empty or have white spaces!',
            },

            'last_name': {
                'required': 'Last name cannot be empty or have white spaces!',
            },

            'country': {
                'required': 'Country cannot be empty or have white spaces!',
            },

            'favourite_cube': {
                'required': 'Favourite cube name cannot be empty or have white spaces!',
            },
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name', ' ')

        value = value.strip()

        if not value:
            raise forms.ValidationError(
                'First name cannot be empty or have white spaces!'
            )

        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name', ' ')

        value = value.strip()

        if not value:
            raise forms.ValidationError(
                'Last name cannot be empty or have white spaces!'
            )

        return value

    def clean_country(self):
        value = self.cleaned_data.get('country', ' ')

        value = value.strip()

        if not value:
            raise forms.ValidationError(
                'Country cannot be empty or have white spaces!'
            )

        return value

    def clean_favourite_cube(self):
        value = self.cleaned_data.get('favourite_cube', ' ')

        value = value.strip()

        if not value:
            raise forms.ValidationError(
                'Favourite cube name cannot be empty or have white spaces!'
            )

        return value

    def clean_bio(self):
        value = self.cleaned_data.get('bio', ' ')

        return value