from typing import Text
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control mb-2", "placeholder": "Enter Username"}), label="")
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"form-control mb-2", "placeholder": "Enter Email ID"}), label="")
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control mb-2", "placeholder": "Enter First Name"}), label="")
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control mb-2", "placeholder": "Enter Last Name"}), label="")
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder": "Enter Password"}), label="")
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder": "Confirm Password"}), label="")
    # captcha = forms.CharField(required=True, )
   
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        
        
    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name'].title()
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
        