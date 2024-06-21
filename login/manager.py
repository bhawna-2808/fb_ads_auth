from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        if password:
            user.set_password(password)
        else:
            # Handle case where no password is provided (e.g., social auth)
            pass
        
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Create and save a staff user with the given email and password.
        """
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a superuser with the given email and password.
        """
        user = self.create_user(email, password=password, is_staff=True, is_superuser=True)
        return user
