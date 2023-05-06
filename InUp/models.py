from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    age = models.CharField(max_length=255, blank=True)
    # age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
