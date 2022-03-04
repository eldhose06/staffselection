from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self,  email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(

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

    def create_superuser(self,  email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    name = models.CharField(max_length=256, default="")
    email = models.EmailField(max_length=32, blank=True, unique=True)  # EmailField
    password = models.CharField(max_length=256, default="")
    date_joined = models.DateField(auto_now_add=True, null=True, blank=True)  # DateTimeField
    dob = models.DateField(null=True)  # DateField
    gender = models.CharField(max_length=256, null=True)
    phoneNumber = models.CharField(max_length=24, null=True)

    institute = models.CharField(max_length=256, null=True)
    post = models.CharField(max_length=256, null=True)

    sslcInstitution = models.CharField(max_length=256, null=True)
    sslc_year_of_study = models.CharField(max_length=256, null=True)
    sslcpercentage = models.CharField(max_length=256, null=True)

    plustwoInstitution = models.CharField(max_length=256, null=True)
    plustwo_year_of_study = models.CharField(max_length=256, null=True)
    plustwopercentage = models.CharField(max_length=256, null=True)

    otherQualification = models.CharField(max_length=256, null=True)

    aadhar = models.CharField(max_length=256, null=True)
    nationality = models.CharField(max_length=256, null=True)
    religion = models.CharField(max_length=256, null=True)
    caste = models.CharField(max_length=256, null=True)
    bloodGroup = models.CharField(max_length=256, null=True)
    handicapped = models.CharField(max_length=256, null=True)

    c_house_name = models.CharField(max_length=256, null=True)
    c_city = models.CharField(max_length=256, null=True)
    c_postoffice = models.CharField(max_length=256, null=True)
    c_district = models.CharField(max_length=256, null=True)
    c_state = models.CharField(max_length=256, null=True)
    c_pincode = models.IntegerField(null=True)  # IntegerField

    last_login = models.DateTimeField(auto_now_add=True, null=True)  # DateTimeField
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Religion(models.Model):
    religion = models.CharField(max_length=256, unique=True)


class Caste(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    caste = models.CharField(max_length=256, unique=True)

class Nationality(models.Model):
    nationality = models.CharField(max_length=256, unique=True)

class Institutes(models.Model):
    instituteName = models.CharField(max_length=256, unique=True)

class Post(models.Model):
    institute = models.ForeignKey(Institutes, on_delete=models.CASCADE)
    postName = models.CharField(max_length=256)
