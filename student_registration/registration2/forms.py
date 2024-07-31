from django import forms
from .models import Student, Project

class StudentForm(forms.ModelForm):
    topic = forms.CharField(max_length=200)
    languages_used = forms.CharField(max_length=200)
    duration = forms.CharField(max_length=50)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
            Project.objects.create(
                student=student,
                topic=self.cleaned_data['topic'],
                languages_used=self.cleaned_data['languages_used'],
                duration=self.cleaned_data['duration']
            )
        return student
