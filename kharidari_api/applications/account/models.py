import uuid as uuid_lib
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .constant import GENDER_CHOICES
from django.core.exceptions import ValidationError


class User(AbstractBaseUser):
    id = models.CharField(default=uuid_lib.uuid4, max_length=50, 
                          editable=False, primary_key=True, unique=True)
    email = models.EmailField(_('Email address'), max_length=250, unique=True, error_messages={'email': 'Email xxists already'})
    first_name = models.CharField(_('First Name'), max_length=250)
    last_name = models.CharField(_('Last Name'), max_length=250, null=True, blank=True)
    password = models.CharField(_('Password'), max_length=250)
    username = None
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    is_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(_('Date of Birth'))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        ordering = ['-created_at']