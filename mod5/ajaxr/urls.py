# registration/urls.py

from django.urls import path
from .views import rregister_student

urlpatterns = [
    path('register/', rregister_student, name='rregister_student'),
]
