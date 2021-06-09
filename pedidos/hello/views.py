from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")#pasar el nombre del template

def angel(request):
    return HttpResponse("Hello, Angel")

def gree(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")#agregar formato al string con f

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })