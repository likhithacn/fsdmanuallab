from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm
from .models import Student

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'registration2/student_deatil.html', {'student': student})

def registerr_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('register_success')
    else:
        form = StudentForm()
    return render(request, 'registration2/registerstudent.html', {'form': form})

def register_success(request):
    return render(request, 'registration2/register_success.html')
