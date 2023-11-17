
from django.urls import path
from .views import cash_register

urlpatterns = [
    path('cash_register/', cash_register, name='cash_register'),
]
