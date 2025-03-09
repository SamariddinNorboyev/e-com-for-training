from django import forms
from .models import Product
from django.core.exceptions import ValidationError
class CreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Product.objects.filter(email = email).exists():
            raise ValidationError(f"Product with {email} exist!")
        return cleaned_data
    

class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Product.objects.exclude(email = self.instance.email).filter(email = email).exists():
            raise ValidationError(f"Product with {email} exist!")
        return cleaned_data