
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import CustomUserModel
from .models import Profile

@receiver(post_save, sender=CustomUserModel)
def my_signal_receiver(sender, instance, created, **kwargs):
    if created:
        print(f"A new instance of {sender} was created: {instance}")
        Profile.objects.create(user = instance)
    else:
        print(f"An instance of {sender} was updated: {instance}")
