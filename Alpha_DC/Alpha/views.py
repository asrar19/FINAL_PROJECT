from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request : HttpRequest):
    return render(request, "Alpha/index.html")


def home(request : HttpRequest):
    return render(request, "Alpha/home.html")

def about(request : HttpRequest):
    return render(request, "Alpha/about.html")
    
def contact(request : HttpRequest):
    return render(request, "Alpha/contact.html")

def vision(request : HttpRequest):
    return render(request, "Alpha/vision.html")

def services(request : HttpRequest):
    return render(request, "Alpha/services.html")


