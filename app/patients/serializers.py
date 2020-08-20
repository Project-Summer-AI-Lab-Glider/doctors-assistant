from rest_framework import serializers
from core.models import Patient, GeneralAnamnesis, PhisicalExamination


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for patient object"""

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('id',)


class GeneralAnamnesisSerializer(serializers.ModelSerializer):
    """Serializer for general amnesis object"""

    class Meta:
        model = GeneralAnamnesis
        fields = '__all__'
        read_only_fields = ('id',)


class PhisicalExaminationSerializer(serializers.ModelSerializer):
    """Serializer for phisical examination object"""

    class Meta:
        model = PhisicalExamination
        fields = '__all__'
        read_only_fields = ('id',)
