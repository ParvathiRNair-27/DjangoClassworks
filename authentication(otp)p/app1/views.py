from tkinter.font import names

from django.contrib.auth.password_validation import password_changed
from django.core.mail import send_mail
from django.db.transaction import commit
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views import View
from app1.forms import SignUpForm
from app1.forms import LoginForm
from app1.models import CustomUser
from django.contrib import messages


#  class based views using view class
class IndexView(View):
    def get(self,request):
        return render(request,'home.html')


class StudentHomeView(View):
    def get(self,request):
        return render(request,'studenthome.html')


class TeacherHomeView(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class AdminHomeView(View):
    def get(self,request):
        return render(request,'adminhome.html')



class SignUpView(View):
    def post(self,request):  # after form submission
        print(request.POST)
        form_instance=SignUpForm(request.POST)
        if(form_instance.is_valid()):
             print(form_instance.cleaned_data)
             user=form_instance.save(commit=False) # when password need to saved encrypted format
             user.is_active=False # after otp verification it will set to true.
             user.save()
             user.generate_otp()
             send_mail(
            "Django Auth OTP",
             user.otp,
            "parvathireji2001@gmail.com",
            [user.email],
            fail_silently=False,)

        return redirect('otp_verify')

    def get(self,request):
        form_instance=SignUpForm()
        return render(request,'signup.html',{'form':form_instance})


class SignInView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if(form_instance.is_valid()):
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            # if username and password is valid "user" returns user object if exist or returns none
            # if user:
            #     # starting session using current session
            #     login(request,user) # adds the current user to the session
            #     # u=request.user
            #     # print(u.name) # prints the current username of the user who has login recently/currently
            #     # print(u.email)
            #     # print(u.first_name)
            #     return redirect('home')


                    # multi user login
                    #------------------
            if user and user.is_superuser==True:
                login(request, user)
                return redirect('adminhome')
            elif user and user.role=="student":
                login(request, user)
                return redirect("studenthome")
            elif user and user.role=="teacher":
                login(request, user)
                return redirect("teacherhome")

            else:
                print("Invalid User credentials")
        return redirect('home')


class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin')


class OtpVerificationView(View):
    def post(self,request):
        otp=request.POST.get('otp')
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('signin')
        except:
            # print("invalid otp")
            messages.error(request, "Invalid OTP.")
            return redirect('otp_verify')

    def get(self,request):
        return render(request,'otp_verify.html')

