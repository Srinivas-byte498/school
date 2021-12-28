import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from student.models import Student


def addStudentView(request):
    try:
        if request.method=="POST":
            dataObjs = json.loads(request.POST.get('data'))
            Student(first_name=dataObjs['first_name'],
                    last_name=dataObjs['last_name'],
                    email=dataObjs['email'],
                    dob=dataObjs['dob'],
                    gender=dataObjs['gender'],
                    ph_num=dataObjs['ph_num'],
                    first_lang=dataObjs['first_lang']).save()
        return JsonResponse({'status':'saved'})
    except Exception as e:
        print(str(e))