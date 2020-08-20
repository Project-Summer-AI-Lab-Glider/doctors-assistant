from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Patient, GeneralAnamnesis, PhisicalExamination
from patients import serializers


class PatientViewSet(viewsets.ModelViewSet):
    """Manage patients in database"""
    queryset = Patient.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PatientSerializer

    def get_queryset(self):
        """Return object for the current authenticated user only"""
        return self.queryset.filter(doctor=self.request.user).order_by('-surname')


class GeneralAnamnesisViewSet(viewsets.ModelViewSet):
    queryset = GeneralAnamnesis.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GeneralAnamnesisSerializer


class PhisicalExaminationViewSet(viewsets.ModelViewSet):
    queryset = PhisicalExamination.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PhisicalExaminationSerializer
