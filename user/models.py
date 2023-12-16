from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import datetime
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
    is_active = models.BooleanField('активный',default=True)
    is_staff = models.BooleanField('сотрудник',default=False)
    is_superuser = models.BooleanField('СуперПользователь',default=False)

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
    name = models.CharField('Название',max_length=100)
    description = models.TextField('Описание')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Exercise(models.Model):
    category = models.ForeignKey(Category, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField('Название',max_length=100)
    description = models.TextField('Описание')
    photo = models.ImageField(upload_to='exercises/')
    day = models.IntegerField('Дата')  # День в программе упражнений

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
    def __str__(self):
        return self.name

from django.db import models

class Nutrition(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    photo = models.ImageField('Фото', upload_to='nutritions/', blank=True, null=True)
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'Питание'
        verbose_name_plural = 'Питания'

    def __str__(self):
        return self.name



class Feedback(models.Model):
    email = models.EmailField('Электронная почта')
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'обратная связь'
    def __str__(self):
        return f"Feedback from {self.email}"