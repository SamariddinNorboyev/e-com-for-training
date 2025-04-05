from django.contrib import admin
from .models import CustomUserModel, Code
# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(Code)