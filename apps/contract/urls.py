# Vendor
from django.urls import path, include
from rest_framework import routers

# Local
from . import views as views

router = routers.SimpleRouter()

router.register(r'contract', views.ContractViewSet, basename="contract")

urlpatterns = [
    path('', include(router.urls)),
]