from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerr_student, name='registerr_student'),
    path('register/success/', views.register_success, name='register_success'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
]
