from django.db import models
from django.conf import settings


class Patient(models.Model):
    """Model representing patient data in database"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male')
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
