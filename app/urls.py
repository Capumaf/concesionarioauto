from django.urls import path
from .views import VehiculoListView

urlpatterns = [
    path('vehiculos', VehiculoListView.as_view(), name='vehiculos_all')
]