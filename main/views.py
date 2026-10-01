from django.shortcuts import render
from .models import Student


def home(request):
    return render(request, 'main/home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'main/student_list.html', {
        'students': students
    })
