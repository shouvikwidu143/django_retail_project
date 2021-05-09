from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('', test_view, name="accounts"),
    path('signup/', signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('profile/', test_view, name="profile"),
]
