from django.db import models
from users.models import CustomUserModel
# Create your models here.
class Profiles(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    user_id = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='account_profiles')