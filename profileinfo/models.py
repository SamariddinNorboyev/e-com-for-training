from django.db import models
from users.models import CustomUserModel
class Profile(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics/')
    bio = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.email