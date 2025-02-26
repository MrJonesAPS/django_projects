from django import forms

class ItemForm(forms.Form):
    text = forms.CharField(max_length=200)
