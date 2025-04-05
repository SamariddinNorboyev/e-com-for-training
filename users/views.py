from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
import requests
from config import settings
from .forms import LoginForm, RegisterModelForm, PasswordResetForm, RestorePasswordForm
from .models import CustomUserModel
from .service import send_email_async

# Create your views here.
class LoginClassView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = CustomUserModel.objects.filter(email = form.cleaned_data['email']).first()
            login(request, user)
            return redirect('order:order_home')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class RegisterClassView(View):
    def get(self, request):
        form = RegisterModelForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = RegisterModelForm(request.POST)
        print('salom')
        if form.is_valid():
            form.save()
            return redirect('users:login')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class LogoutClassView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


def google_loging(request):
    auth_url = (
        f"{settings.GOOGLE_AUTH_URL}"
        f"?client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )
    return redirect(auth_url)
def google_callback(request):
    code = request.GET.get('code')
    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = requests.post(settings.GOOGLE_TOKEN_URL, data=token_data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    user_info_response = requests.get(settings.GOOGLE_USER_INFO_URL, headers={"Authorization": f"Bearer {access_token}"})
    user_info = user_info_response.json()
    user, created = CustomUserModel.objects.get_or_create(google_id=user_info.get('id'), email=user_info.get('email'),
                                                          image=user_info.get('picture'),
                                                          first_name=user_info.get('given_name'),
                                                          last_name=user_info.get('family_name'))
    login(request, user)
    return redirect('order:order_home')





class PasswordResetView(View):
    def get(self, request):
        form = PasswordResetForm()
        return render(request, 'users/reset-password.html', {'form': form})
    def post(self, request):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            #send code
            email = form.cleaned_data.get('email')
            send_email_async(email)
            return redirect('users:restore_password')
        form = PasswordResetForm()
        return render(request, 'users/reset-password.html', {'form': form})



class RestorePasswordView(View):
    def get(self, request):
        form = RestorePasswordForm()
        return render(request, 'users/restore-password.html', {'form': form})
    def post(self, request):
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            new_password = form.cleaned_data.get('new_password')
            user = CustomUserModel.objects.filter(email=email).first()
            user.set_password(new_password)
            user.save()
            return redirect('users:login')
        form = RestorePasswordForm()
        return render(request, 'users/restore-password.html', {'form': form})


def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})