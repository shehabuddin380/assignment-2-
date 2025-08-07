# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def assign_group_to_user(sender, instance, created, **kwargs):
    if created and not instance.groups.exists():
        group = Group.objects.get(name='Participant')
        instance.groups.add(group)
