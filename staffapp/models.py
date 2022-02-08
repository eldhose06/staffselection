from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        # user.set_unusable_password(password)
        user.save(using=self._db)
        return user

    def create_complete_user(self, name, email, dob, gender, phoneNumber,  password=None):
        if not phoneNumber:
            raise ValueError('Users must have a phone Number')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=CustomUserManager.normalize_email(email),
            password=password,
            dob=dob,
            gender=gender,
            phoneNumber=phoneNumber,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    # applicationNo = models.CharField(unique=True, max_length=256, null=True, db_index=True)  # IntegerField
    name = models.CharField(max_length=256, default="")
    email = models.EmailField(max_length=32, blank=True, unique=True)  # EmailField
    password = models.CharField(max_length=256, default="")
    date_joined = models.DateField(auto_now_add=True, null=True, blank=True)  # DateTimeField
    dob = models.DateField(null=True)  # DateField
    gender = models.CharField(max_length=256, null=True)
    phoneNumber = models.CharField(max_length=24, null=True)

    last_login = models.DateTimeField(auto_now_add=True, null=True)  # DateTimeField
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
