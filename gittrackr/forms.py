# forms.py
from django import forms

class CreateFolderForm(forms.Form):
    folder_name = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={'class': 'w-96 border-none focus:outline-none no-underline focus:border-none mx-5 custom-focus', 'placeholder' : 'ex. PPL PRAK I2'},)
    )