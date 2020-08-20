from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Patient(models.Model):
    """Model representing patient basic personal data"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')],
                           default='male')
    phone = models.CharField(max_length=20, default='0')
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class GeneralAnamnesis(models.Model):
    """
    Model representing patient's general anamnesis.
    NOTE: w1 - first aspect from the excel "Wywiad".
    """
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    w1 = models.CharField(max_length=1000, default="do rozważenia dosłowny zapis pierwszych zdań pacjenta")
    w2 = models.CharField(max_length=255)
    w3a = models.CharField(max_length=255, choices=[('obecne', 'obecne'), ('nieobecne', 'nieobecne')])
    w3b = models.CharField(max_length=255)
    w4 = models.CharField(max_length=255)


class PhisicalExamination(models.Model):
    """
    Model representing patient's phisical examination.
    NOTE: p1 - first aspect from the excel "Badanie fizykalne".
    """
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    p1 = models.CharField(max_length=255, choices=[('stan dobry', 'stan dobry'), ('stan średni', 'stan średni'),
                                                   ('stan ciężki', 'stan ciężki')])
    p2 = models.CharField(max_length=255)
    p3 = models.CharField(max_length=255)
    p4 = models.CharField(max_length=255)
    p5 = models.CharField(max_length=255,
                          choices=[('normosteniczna', 'normosteniczna'), ('hyposteniczna', 'hyposteniczna'),
                                   ('hypersteniczna', 'hypersteniczna')])

