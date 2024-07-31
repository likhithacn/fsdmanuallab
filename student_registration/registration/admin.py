from django.contrib import admin
from .models import Student, Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    list_filter = ('course',)  # Enables filtering enrollments by course
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
 