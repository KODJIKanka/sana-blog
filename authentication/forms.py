from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SinupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','email','role')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label='identifiant')
    password = forms.CharField(max_length=60, widget= forms.PasswordInput, label='Mot de passe')