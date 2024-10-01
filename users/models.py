from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, admission_number, password=None):
        if not admission_number: raise ValueError("The Admission Number Field is Required")
        user = self.model(admission_number=admission_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, admission_number, password=None):
        user = self.create_user(admission_number, password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    admission_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'admission_number'

    def __str__(self):
        return self.admission_number
