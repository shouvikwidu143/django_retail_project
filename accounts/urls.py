from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', test_view, name="accounts"),
    path('signup/', signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('profile/', profile, name="profile"),
    path('profile/edit/', edit_profile, name="profile-edit"),
    path('profile/addresses/', addresses_view, name="addresses"),
    path('profile/addresses/<int:pk>/delete', AddressDeleteView.as_view(), name='address-delete'),
    path('profile/addresses/new', AddressCreateView.as_view(), name='address-new'),
    path('profile/addresses/<int:pk>/edit', AddressUpdateView.as_view(), name='address-edit'),
    path('profile/addresses/<int:pk>/default', AddressSetDefaultView.as_view(), name='address-default'),
]
