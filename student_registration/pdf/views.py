# registration/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Student
from .resources import StudentResource
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ExportCSVView(View):
    def get(self, request):
        student_resource = StudentResource()
        dataset = student_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        return response

class ExportPDFView(View):
    def get(self, request):
        students = Student.objects.all()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        y = 750
        for student in students:
            p.drawString(100, y, f"Name: {student.first_name} {student.last_name}")
            p.drawString(100, y - 20, f"Email: {student.email}")
            y -= 40

        p.showPage()
        p.save()

        return response
