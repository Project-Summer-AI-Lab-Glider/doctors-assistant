from rest_framework import serializers
from core.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for patient object"""

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname']
        read_only_fields = ('id', )
