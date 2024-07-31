from django.shortcuts import render

def index(request):
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    students = ['Alice','Bob','Charlie','David']
    finalList = []
    
    for student in students:
        if student.startswith('B'):
            finalList.append(student)

    context = {
        'fruits': fruits,
        'students': finalList,
    } 
    return render(request, 'listfruitapp/index.html', context)
