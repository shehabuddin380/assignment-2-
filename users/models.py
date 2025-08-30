from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r'^\+?\d{9,15}$', "Phone number must be in the format: '+8801XXXXXXXXX'.")]
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.jpg',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
