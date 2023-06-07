from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields: dict):
        if not email:
            raise ValueError(_('Email is required field'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email: str, password: str, **extra_fields: dict):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super User must be registered as staff.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Super User must be active.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super User flag must be selected'))
        
        return self.create_user(email, password, **extra_fields)