from django import forms


class LoginForm(forms):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
