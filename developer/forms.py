from django import forms

class dev_info(forms.Form):
    name = forms.CharField(max_length=20,)
    password = forms.CharField(max_length=20,)
