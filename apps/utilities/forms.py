# forms.py
from django import forms

class AddRepositoryForm(forms.Form):
    repository_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-96 mx-4 border-2 rounded-xl m-4', 'placeholder' : 'ex. DjangoEcommerce'},)
        )