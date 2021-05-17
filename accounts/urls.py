from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', test_view, name="accounts"),
    path('signup/', signup_view, name="signup"),
    path("social/signup/", SocialSignUpView.as_view(), name="socialaccount_signup"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('profile/', profile, name="profile"),
    path('profile/edit/', edit_profile, name="profile-edit"),
    path('profile/addresses/', addresses_view, name="addresses"),
    path('profile/addresses/<int:pk>/delete/', AddressDeleteView.as_view(), name='address-delete'),
    path('profile/addresses/new/', AddressCreateView.as_view(), name='address-new'),
    path('profile/addresses/<int:pk>/edit/', AddressUpdateView.as_view(), name='address-edit'),
    path('profile/addresses/<int:pk>/default/', AddressSetDefaultView.as_view(), name='address-default'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/password-change', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('profile/password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
