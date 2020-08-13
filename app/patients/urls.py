from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.patients import views

router = DefaultRouter()
router.register('tags', views.PatientViewSet)

app_name = 'patients'

urlpatterns = [
    path('', include(router.urls))
]