"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name="home"),
    path('signup',views.SignUpView.as_view(),name="signup"),
    path('signin',views.SignInView.as_view(),name="signin"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('otp_verify',views.OtpVerificationView.as_view(),name="otp_verify"),
    path('adminhome',views.AdminHomeView.as_view(),name="adminhome"),
    path('studenthome',views.StudentHomeView.as_view(),name="studenthome"),
    path('teacherview',views.TeacherHomeView.as_view(),name="teacherhome"),
    path('accounts/',include('django.contrib.auth.urls')),



]
