from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from .models import Reader  # Ensure the model name is correct

# Create your views here.

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def readers(request):
    return render(request, "readers.html", context={"current_tab": "readers"})

def books(request):
    return render(request, "books.html", context={"current_tab": "books"})

def returns(request):
    return render(request, "returns.html", context={"current_tab": "returns"})

def my_bag(request):
    return render(request, "my_bag.html", context={"current_tab": "my_bag"})

def readers_tab(request):
    readers_list = Reader.objects.all() 
    return render(request, "readers.html", context={"current_tab": "readers", "readers": readers_list})

def save_reader(request):
    if request.method == "POST":  # Ensure the request is POST
        reference_id = request.POST.get("reference_id", "").strip()
        reader_name = request.POST.get("reader_name", "").strip()
        reader_contact = request.POST.get("reader_contact", "").strip()
        reader_address = request.POST.get("reader_address", "").strip()

        if not reference_id or not reader_name or not reader_contact or not reader_address:
            return HttpResponse("All fields are required", status=400)

        reader_item = Reader(
            reference_id=reference_id,
            reader_name=reader_name,
            reader_contact=reader_contact,
            reader_address=reader_address,
            active=True
        )
        reader_item.save()
        return redirect("/readers")  # Redirect after successful save
    
    return HttpResponse("Invalid request", status=405)  # If method is not POST, return an error
