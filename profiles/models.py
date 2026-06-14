from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    phone   = models.CharField(max_length=15, blank=True)
    city    = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    bio     = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - Profile"


# ✅ Har naye User ke saath automatically Profile banega
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)