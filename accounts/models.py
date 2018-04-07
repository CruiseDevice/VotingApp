from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, unique=True)
    # password field defined in base class
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' # email can be used as username

    def __str__(self):
        return self.email

    