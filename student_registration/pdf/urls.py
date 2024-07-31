# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('export/csv/', views.ExportCSVView.as_view(), name='export_csv'),
    path('export/pdf/', views.ExportPDFView.as_view(), name='export_pdf'),
]
