from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#
#         if username is None:
#             raise TypeError('Users should have a username')
#         if email is None:
#             raise TypeError('Users should have a Email')
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#     def create_superuser(self, username, email, password=None):
#
#         if password is None:
#             raise TypeError('Password should not  be None')
#
#
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=256, default="")
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     password = models.CharField(max_length=256, default="")
#     gender = models.CharField(max_length=256, null=True)
#     phoneNumber = models.CharField(max_length=24, null=True)
#     dob = models.DateField(null=True)  # DateField
#     # username = models.CharField(max_length=255, unique=True, db_index=True)
#
#     is_verified = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email
#
#     def tokens(self):
#         return ''
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
from staffapp.managers import CustomUserManager

#
# class User(AbstractBaseUser):
#     # applicationNo = models.CharField(unique=True, max_length=256, null=True, db_index=True)  # IntegerField
#     name = models.CharField(max_length=256, default="")
#     email = models.EmailField(max_length=32, blank=True, unique=True)  # EmailField
#     password = models.CharField(max_length=256, default="")
#     date_joined = models.DateField(auto_now_add=True, null=True, blank=True)  # DateTimeField
#     dob = models.DateField(null=True)  # DateField
#     gender = models.CharField(max_length=256, null=True)
#     phoneNumber = models.CharField(max_length=24, null=True)
#
#     last_login = models.DateTimeField(auto_now_add=True, null=True)  # DateTimeField
#     is_verified = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     username = None
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.name
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, name=None, birthday=None, gender=None,phoneNumber=None,password=None
#                     ):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             Email=self.normalize_email(email),
#             name=self.normalize_email(email),
#             Date_of_Birth=birthday,
#             gender=gender,
#             phoneNumber=phoneNumber,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, Email_Address, password):
#         user = self.create_user(
#             Email_Address=self.normalize_email(Email_Address),
#             password=password,
#         )
#         user.is_admin = True
#         user.is_active=True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
# class Users(AbstractBaseUser):
#     Email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
#     Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
#     name = models.CharField(max_length=30, blank=True, null=True)
#     username= models.CharField(max_length=30,unique=True, blank=True, null=True)
#     gender = models.CharField(max_length=30, blank=True, null=True)
#     phoneNumber = models.CharField(max_length=30, blank=True, null=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'Email'
#
#     objects = MyAccountManager()
#
#     class Meta:
#         db_table = "tbl_users"
#
#     def __str__(self):
#         return str(self.email)
#
#
#     def has_perm(self, perm, obj=None): return self.is_superuser
#
#     def has_module_perms(self, app_label): return self.is_superuser

