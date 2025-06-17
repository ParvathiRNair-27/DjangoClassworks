from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
class HomeView(View):
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

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})
    def post(self,request):
         form_instance=SignupForm(request.POST)
         if form_instance.is_valid():
             user=form_instance.save(commit=False) #after otp verfication it will set to true
             user.is_active=False
             user.save()
             user.generate_otp()
             #send otp to email or phone
             send_mail(
                 "Django Auth OTP",
                 user.otp,
                 "parvathireji2001@gmail.com",
                 [user.email],
                 fail_silently=False,
             )
         return redirect('verify')
             # form_instance.save()
             # # user=form_instance.save(commit=False)
             # # user.set_password(form_instance.cleaned_data['password'])
             # # user.save()
             # return redirect('home')




from django.contrib.auth import authenticate,login
from app1.forms import LoginForm
class SigninView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            # if user:
            #     login(request,user)
            #     # u=request.user
            #     # print(u.username)
            #     # print(u.email)
            #     # print(u.last_name)
            #     return redirect('home')
            if user and user.is_superuser==True:
                login(request, user)
                return redirect('ahome')
            elif user and user.role=="student":
                login(request, user)
                return redirect('shome')
            elif user and user.role=="teacher":
                login(request, user)
                return redirect('thome')
            else:
                print('invalid user credential')
        return redirect('home')

            # user=User.objects.get(username=name)
            # if(user.password==pwd):
            #     "valid"
            # else:
            #     "Invalid"
            #
from django.contrib.auth import logout
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('SigninView')

from app1.models import CustomUser
class OtpVerificationView(View):

    def post(self,request):
        otp=request.POST.get('otp')
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            return redirect('Signinview')
        except:
            # print("invalid otp")
            messages.error(request,"Invalid OTP")
            return redirect('verify')
    def get(self,request):
        return render(request,'otp_verify.html')


