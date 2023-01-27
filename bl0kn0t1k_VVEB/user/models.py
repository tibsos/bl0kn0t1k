from django.db import models as m

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE, related_name = 'profile')

    name = m.CharField(max_length = 100)

    initials = m.CharField(max_length = 3)

    dark_mode = m.BooleanField(default = False)

    password_recovery_token = m.TextField(blank = True)

    def __str__(self):
        
        return self.name

    class Meta:

        ordering = ['-name']

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Profile.objects.create(user = instance)
    