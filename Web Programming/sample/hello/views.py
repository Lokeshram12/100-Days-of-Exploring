from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world! This is the index view of the hello app.")

def greet(request, name):
    return HttpResponse(f"Hello, {name}! Welcome to the hello app.")

def indexUsingTemplate(request):
    return render(request, 'hello/index.html')

def greetUsingTemplate(request, name):
    return render(request, 'hello/greet.html', {'name': name})