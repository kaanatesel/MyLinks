from django import forms

from .models import User

class RegisterForm(forms.Form):
    nickname = forms.CharField(label="Nickname",error_messages={'required': 'Please enter your nickname'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(label="First Name",error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label="Last Name", error_messages={'required': 'Please enter your last name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email Adress",error_messages={'required': 'Please enter an email address'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    aggrewithterm = forms.BooleanField(error_messages={'required': 'Aggree with terms of use'})

class LoginForm(forms.Form):
    nickname = forms.CharField(label="Nickname Adress",error_messages={'required': 'Please enter an email address'}, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','placeholder':'Nickname'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm','placeholder':'Password'}))