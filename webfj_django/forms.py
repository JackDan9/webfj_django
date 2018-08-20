# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    """
    LoginForm
    """
    uid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'uid', 'placeholder': 'Username'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pwd', 'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    """
    RegisterForm
    """
    username = forms.CharField(label='username', max_length=100,
                               widget=forms.TextInput(attrs={'id': 'username', 'onblur': 'authentication'}))
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class SetInfoForm(forms.Form):
    """
    SetInfoForm
    """
    username = forms.CharField()

# class SearchForm(forms.Form):
    # keyword = forms.CharField(widget=forms.TextInput)