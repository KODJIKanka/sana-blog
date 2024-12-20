from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(max_length=50,label='Nom du groupe')