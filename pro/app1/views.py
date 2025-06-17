from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse   ##importing

#home view

def home(request):

    return HttpResponse("Django")

#index view
def index(request):
    return HttpResponse("Index Page")

