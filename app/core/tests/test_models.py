from django.test import TestCase
from django.contrib.auth import get_user_model

# from core import models


def sample_user(email='test@test.com', password='Test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


# class ModelTests(TestCase):
#
#     def test_patient_str(self):
#         """Test the patient string representation"""
#         patient = models.Patient.objects.create(
#
#         )
