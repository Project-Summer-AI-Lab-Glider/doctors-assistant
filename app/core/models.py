from django.db import models
from django.conf import settings


class Patient(models.Model):
    """Model representing patient data in database"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    height = models.IntegerField
    weight = models.IntegerField
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name + '' + self.surname
