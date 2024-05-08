from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    profile_pic=models.ImageField(upload_to="media",blank=True,null=True)
    address = models.TextField()
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

# Create your models here.
