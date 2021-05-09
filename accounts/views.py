from django.shortcuts import render, HttpResponse, redirect
from .forms import UserSignUpForm
from django.contrib import messages
from django.conf import settings
from .controllers import *

# Create your views here.

def test_view(request):
    return HttpResponse("I am god")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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