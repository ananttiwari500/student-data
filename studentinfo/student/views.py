from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import StudentData

def student_list(request):
    MAX_OBJECTS = 20
    stu = StudentData.objects.all()[:MAX_OBJECTS]
    data = {"results": list(stu.values("first_name", "last_name", "number"))}
    return JsonResponse(data)


def student_detail(request, pk):
    stud = get_object_or_404(StudentData, pk=pk)
    data = {"results": {
        "first_name": stud.first_name,
        "last_name": stud.last_name,
        "number": stud.number
    }}
    return JsonResponse(data)





# def create(request):
#     form = StudentForm()
#     context = {}
#     return render(request, "create.html", context= context )








