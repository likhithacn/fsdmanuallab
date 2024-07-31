from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    # module4
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    # module5
    path('search', views.search_students, name='search_students'),
]


 
