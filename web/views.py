from django.shortcuts import render

# Create your views here.
from student.models import Student


def addStudent(request):
    return render(request, "add_student.html")

def stdList(request):
    students=Student.objects.all().values('first_name','last_name','gender','email','ph_num','first_lang')
    return render(request, "std_list.html",{'students':students})