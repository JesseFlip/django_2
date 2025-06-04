from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def jesse(request):
    return HttpResponse("Jesse's on it!")

def david(request):
    return HttpResponse("Hey, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })