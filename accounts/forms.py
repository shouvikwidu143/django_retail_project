from typing import Text
from allauth.socialaccount.forms import SignupForm
from allauth.socialaccount.adapter import get_adapter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


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
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data
    
class UserUpdateForm(forms.ModelForm):
    """docstring for UserUpdateForm"forms.ModelFormf __init__(self, arg):"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'about_me']
        
# class AdressUpdateMetaForm(forms.ModelForm):
    
#     class Meta:
#         model = Addresses
#         fields = ['contact_name', 'contact_number', 'address_type',
#               'address_1', 'address_2', 'nearby_location',
#               'city_or_district', 'state', 'country','pincode',
#               'delivery_instructions', 'is_primary_address'
#               ]
    
#     def save(self, commit=True):
#         address = super(AdressUpdateMetaForm, self).save(commit=False)
#         address.is_primary_address = is_primary_address = self.cleaned_data['is_primary_address']
#         if is_primary_address:
#             all_addresses = Addresses.objects.filter(profile__id = self.request.user.profile.id)
#             print(self.request.user.profile.id)
#             print(all_addresses)
#             for _each in all_addresses:
#                 if _each.profile != self.request.user.profile:
#                     _each.is_primary_address = False
#                     _each.save()

#         if commit:
#             address.save()

#         return address
