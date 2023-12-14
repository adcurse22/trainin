from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным email и паролем.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с введенным email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    category = models.ForeignKey(Category, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='exercises/')
    day = models.IntegerField()  # День в программе упражнений

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='nutrition', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='nutrition/')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.email}"