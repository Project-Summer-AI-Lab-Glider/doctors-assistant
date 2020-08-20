from django.urls import path, include
from rest_framework.routers import DefaultRouter

from patients import views

router = DefaultRouter()
router.register('patients', views.PatientViewSet)
router.register('generalanamnesis', views.GeneralAnamnesisViewSet)
router.register('phisicalexamination', views.PhisicalExaminationViewSet)

app_name = 'patients'

urlpatterns = [
    path('', include(router.urls))
]