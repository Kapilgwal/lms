from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

# Create your views here.

def home(request):
    return render(request,"home.html",context={"current_tab" : "home"})


def readers(request):
    return render(request,"readers.html",context={"current_tab" : "readers"})


def books(request):
    return render(request,"books.html",context={"current_tab" : "books"})


def returns(request):
    return render(request,"returns.html",context={"current_tab" : "returns"})


def my_bag(request):
    return render(request,"my_bag.html",context={"current_tab" : "my_bag"})


# def shopping(request):
#     return HttpResponse("Hello World for shopping")

# def save_student(request):
#     name = request.POST['student_name']
#     return HttpResponse(f"Welcome to libaray : {name}")