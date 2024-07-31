from django.urls import path
from . import views

urlpatterns = [
    path('', views.datetime_offset, name='datetime_offset'),
]
