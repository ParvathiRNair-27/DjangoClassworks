

from django import forms
from django.forms import PasswordInput


#Addition
class AdditionForm(forms.Form):    #form structure definition
    number1=forms.IntegerField()
    number2=forms.IntegerField()


#Factorial
class FactorialForm(forms.Form):    #form structure definition
    number=forms.IntegerField()


#BMI
class BMIForm(forms.Form):    #form structure definition
    Height=forms.IntegerField()
    Weight=forms.IntegerField()

#SIGNUP
class SignupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    email=forms.EmailField()
    gender_choices=[('male',"Male"),('female',"Female")]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    role_choices=[('admin',"Admin"),('student',"Student")]
    role=forms.ChoiceField(choices=role_choices)

##CALORIE
class CalorieForm(forms.Form):
    gender_choices = [('male', "Male"), ('female', "Female")]
    Gender = forms.ChoiceField(choices=gender_choices)

    Weight=forms.IntegerField()
    Height=forms.IntegerField()
    Age=forms.IntegerField()
    activity_choices=[(1.2,"Sedentary"),(1.375,"Lightly Active"),(1.55,"Moderately Active"),(1.75,"Very Active"),(1.9,"Extra Active")]
    Activity_level=forms.ChoiceField(choices=activity_choices)
