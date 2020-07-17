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

class ChanageUserInforForm(forms.Form):
    firstname = forms.CharField(label="First Name",error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label="Last Name", error_messages={'required': 'Please enter your last name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))

class UserDesForm(forms.Form):
    Description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "class":"form-control form-control-lg"}))


COLOR_CHOICES= [
    (' #ffe6e6', 'Red'),
    ('#ccebff', 'Blue'),
    ('#f5ccff', 'Purple'),
    ('#ffffcc', 'Yellow'),
    ]


class LinkForm(forms.Form):
    linkname = forms.CharField(label="Link Name",error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.CharField(label="Url",error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(label="Color", widget=forms.Select(choices=COLOR_CHOICES,attrs={'class': 'form-control'}))