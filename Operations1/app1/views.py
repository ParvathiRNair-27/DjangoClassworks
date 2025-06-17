from django.shortcuts import render

# Create your views here.
#Addition
from app1.forms import AdditionForm

from app1.forms import SignupForm


def addition(request):
    if(request.method=='POST'):
        print(request.POST)
     #GET Request
    form_instance=AdditionForm()       #empty form object
    return render(request, 'addition.html',{'form':form_instance})

#Factorial
from app1.forms import FactorialForm
def factorial(request):
    if (request.method == 'POST'):
        print(request.POST)
    form_instance = FactorialForm()
    return render(request, 'factorial.html',{'form':form_instance})


#BMI
from app1.forms import BMIForm
def bmi(request):
    if (request.method == 'POST'):
        print(request.POST)
        # GET Request
    form_instance = BMIForm()
    return render(request, 'bmi.html',{'form':form_instance})

##SIGN up
from app1.forms import SignupForm
def signup(request):
    if (request.method == 'GET'):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})

##Calorie req
from app1.forms import CalorieForm
def calorie(request):
    if(request.method=='POST'):  ##after form submission
        print(request.POST)

        ##creating form object using data submitted by user
        form_instance=CalorieForm(request.POST)

        ##checks the validity of data using is_valid()
        if form_instance.is_valid():

            ##accessing the cleaned data after validation
            data=form_instance.cleaned_data
            Height=(data['Height'])
            Weight=(data['Weight'])
            print(type('Height'))
            Gender=(data['Gender'])
            Age=(data['Age'])
            Activity_level=(data['Activity_level'])
            print(type(Activity_level))
            print(Height,Weight,Gender,Age,Activity_level)




            if Gender=='male':
                bmr=((10*Weight)+(6.25*Height)-(5*Age)+5)

            else:
                bmr=((10*Weight)+(6.25*Height)-(5*Age)-161)

            calorie=bmr*float(Activity_level)
            print(calorie)

        return render(request, 'calorie.html',{'form':form_instance,'result':calorie})

    form_instance=CalorieForm()
    return render(request,'calorie.html',{'form':form_instance})