# forms.py
from django import forms

class MyForm(forms.Form):
    label = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
