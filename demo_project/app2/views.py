from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#home view
def home(request):
    # return HttpResponse("Welcome to Home")
    context={'name':'Arun','age':25}
    return render(request,'home.html',context)

#first view
def first(request):
    # return HttpResponse("First Page")
    return render(request,'first.html')                 #html folders in template folder

#second view
def second(request):
    # return HttpResponse("Second Page")
    return render(request,'second.html')