from django.contrib import admin
from .models import Student, Project

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'topic', 'languages_used', 'duration')
    search_fields = ('student__first_name', 'student__last_name', 'topic')
