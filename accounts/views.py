from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.conf import settings
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from allauth.socialaccount.views import SignupView
from .forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm #, AdressUpdateMetaForm
from .controllers import *
from .models import *

# Create your views here.

def test_view(request):
    return HttpResponse("I am god")
    # csrfmiddlewaretoken: 4SRz3ohIszml6ixra9UlbEv8FQogdHvPXZIDaKOd0yUqaXwTef9qJjPPulxdCvYr
    # username: shouvik
    # password1: Sdas@9800
    # password2: Sdas@9800

class SocialSignUpView(SignupView):
    template_name = 'accounts/social_signup.html'
        
@user_unauthenticated
def signup_view(request):
    errors = []
    if request.method == 'POST':
        captcha_value = request.POST.get("captcha")
        form = UserSignUpForm(request.POST)
        if captcha_value == settings.CAPTCHA_STRING:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your {username} account has been created. You can login now.')
                return redirect('home')
        else:
            errors.append("Invalid Captcha")
    else:
        settings.CAPTCHA_STRING = random_string = generate_random_string(6)
        generate_captch(random_string, settings.MEDIA_ROOT+"/captcha/captcha.png")
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, "captcha":"captcha.png", "errors":errors})
    
@login_required
def profile(request):
    profile_data = Profile.objects.filter(user__username = request.user.username)
    context = {
        'profile_data': profile_data
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    errors = []
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        captcha_value = request.POST.get("captcha")
        if captcha_value == settings.CAPTCHA_STRING:
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                
                messages.success(request, f'Your account has been updated succefully.')
                return redirect('profile')
        else:
            errors.append("Invalid Captcha")
    else:
        settings.CAPTCHA_STRING = random_string = generate_random_string(6)
        generate_captch(random_string, settings.MEDIA_ROOT+"/captcha/captcha.png")
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'captcha': 'captcha.png',
        'errors':errors
    }
    return render(request, 'accounts/profile_edit.html', context)

@login_required
def addresses_view(request):
    addresses_data = Addresses.objects.filter(profile__id = request.user.profile.id)
    context = {
        'addresses_data': addresses_data
    }
    return render(request, 'accounts/addresses.html', context)

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Addresses
    template_name = 'accounts/address_create_update.html'
    fields = ['contact_name', 'contact_number', 'address_type',
              'address_1', 'address_2', 'nearby_location',
              'city_or_district', 'state', 'country','pincode',
              'delivery_instructions', 'is_primary_address'
              ]

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        is_primary_address = form.instance.is_primary_address
        if is_primary_address:
            addresses_data = Addresses.objects.filter(profile__id = self.request.user.profile.id,is_primary_address=True)
            for _each_address in addresses_data:
                if _each_address.id != form.instance.id:
                    _each_address.is_primary_address = False
                    _each_address.save()
        return super().form_valid(form)

class AddressDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Addresses
    template_name = 'accounts/address_delete.html'  # <apps>/<model>_<viewtype>.html
    context_object_name = 'address'
    success_url = '/accounts/profile/addresses'

    def test_func(self):
        addresses = self.get_object()
        if self.request.user == addresses.profile.user:
            return True
        return False
    
class AddressUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Addresses
    template_name = 'accounts/address_create_update.html'
    # form_class = AdressUpdateMetaForm
    fields = ['contact_name', 'contact_number', 'address_type',
              'address_1', 'address_2', 'nearby_location',
              'city_or_district', 'state', 'country','pincode',
              'delivery_instructions', 'is_primary_address'
              ]

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        is_primary_address = form.instance.is_primary_address
        if is_primary_address:
            addresses_data = Addresses.objects.filter(profile__id = self.request.user.profile.id,is_primary_address=True)
            for _each_address in addresses_data:
                if _each_address.id != form.instance.id:
                    _each_address.is_primary_address = False
                    _each_address.save()
                    
        return super().form_valid(form)

    def test_func(self):
        addresses = self.get_object()
        if self.request.user == addresses.profile.user:
            return True
        return False
    
class AddressSetDefaultView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Addresses
    template_name = 'accounts/address_set_default.html'
    fields = ['is_primary_address']
    
    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        is_primary_address = form.instance.is_primary_address
        if is_primary_address:
            addresses_data = Addresses.objects.filter(profile__id = self.request.user.profile.id,is_primary_address=True)
            for _each_address in addresses_data:
                if _each_address.id != form.instance.id:
                    _each_address.is_primary_address = False
                    _each_address.save()
                    
        return super().form_valid(form)

    def test_func(self):
        addresses = self.get_object()
        if self.request.user == addresses.profile.user:
            return True
        return False
    
class WishListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = WishList
    template_name = 'accounts/user_wishlist.html' 
    context_object_name = 'wish_list_items'
    
    def test_func(self):
        wish_list_owner = get_object_or_404(WishList, wishlist_name=self.kwargs.get('user_wishlist'))
        if self.request.user != wish_list_owner.user:
            return False
        return True
    
    def get_queryset(self):
        wish_list_owner = get_object_or_404(WishList, wishlist_name=self.kwargs.get('user_wishlist'))
        return WishListItem.objects.filter(user_wishlist=wish_list_owner)

        