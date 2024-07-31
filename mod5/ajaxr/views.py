# registration/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import StudentForm
def rregister_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
    # You can perform additional operations here, like sending an email, etc.
        return JsonResponse({'success': True})
    else:
        form = StudentForm()
        return render(request, 'ajaxr/regajax.html', {'form': form})
   
