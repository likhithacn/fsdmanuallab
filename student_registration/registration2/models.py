from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"Project for {self.student}: {self.topic}"
