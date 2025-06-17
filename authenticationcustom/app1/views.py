from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm


# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')



class SignUpView(View):

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})
    def post(self,request):
         form_instance=SignupForm(request.POST)
         if form_instance.is_valid():
             form_instance.save()
             # user=form_instance.save(commit=False)
             # user.set_password(form_instance.cleaned_data['password'])
             # user.save()
             return redirect('home')




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
            if user:
                login(request,user)
                u=request.user
                print(u.username)
                print(u.email)
                print(u.last_name)
                return redirect('home')
            else:
                print('invalid user credential')
                return redirect('SigninView')

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


