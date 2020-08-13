from rest_framework import serializers
from app.core.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    """Serializer for patient object"""

    class Meta:
        model = Patient
        fields = {'id', 'name'}
        read_only_fields = {'id',}