from django.shortcuts import render

# Create your views here.

def log_in(request):
    return render(request, "log_in.html")

def home(request):
    return render(request, "home.html")
