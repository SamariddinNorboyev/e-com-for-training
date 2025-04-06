from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from order.urls import app_name
from . import views


app_name = 'users'
urlpatterns = [
    path('login/google/', views.google_loging, name='google_login'),
    path('google/login/callback/', views.google_callback, name='google_callback'),
    path('login/', views.LoginClassView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutClassView.as_view(), name='logout'),
    path('register/', views.RegisterClassView.as_view(), name='register'),
    path('reset-password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('restore-password/', views.RestorePasswordView.as_view(), name='restore_password'),
]