from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import CustomUserModel, Code




class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(email = email, password = password)
        if not user:
            raise ValidationError('Email yoki Password xato')
        return cleaned_data





class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def save(self):
        user = CustomUserModel.objects.create_user(**self.cleaned_data)
        return user



class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if not CustomUserModel.objects.filter(email=email).exists():
            raise ValidationError('email topilmadi')
        return cleaned_data



class RestorePasswordForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    code = forms.IntegerField(max_value=9999, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        code = cleaned_data.get('code')
        new_password = cleaned_data.get('new_password')
        re_password = cleaned_data.get('re_password')
        if new_password != re_password:
            return ValidationError('Yangi password va re-password teng emas')
        user = CustomUserModel.objects.filter(email = email).first()
        if not user:
            raise ValidationError(f"{email} topilmadim")
        if not Code.objects.filter(user=user, code=code, expiration_date__gt=timezone.now()):
            raise ValidationError(f"code topilmadi {timezone.now()}")
        return cleaned_data

