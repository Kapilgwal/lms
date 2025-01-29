from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

# Create your views here.

def home(request):
    return render(request,"index.html",context={})


def shopping(request):
    return HttpResponse("Hello World for shopping")

def save_student(request):
    name = request.POST['student_name']
    return HttpResponse(f"Welcome to libaray : {name}")