# forms.py
from django import forms

class AddRepositoryForm(forms.Form):
    repository_name = forms.CharField(label='Repository Name', max_length=100)