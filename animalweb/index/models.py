from django.db import models
from django.contrib.auth.models import User

class Selling(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    animal_name = models.CharField(max_length=100)
    animal_image = models.ImageField(upload_to='animal_image/')
    animal_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username