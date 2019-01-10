from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def studentlist(request):
    s=Student.objects.all()
    data={"results":list(s.values('sid','sname','fee','email'))}
    return JsonResponse(data)

