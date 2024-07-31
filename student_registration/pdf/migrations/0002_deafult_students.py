# registration/migrations/0002_default_students.py

from django.db import migrations
from pdf.models import Student

def add_default_students(apps, schema_editor):
    Student.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
    Student.objects.create(first_name='Jane', last_name='Smith', email='jane.smith@example.com')

class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_students),
    ]
