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
from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studenthome',views.StudentHomeView.as_view(),name="shome"),
    path('teacherhome',views.TeacherHomeView.as_view(),name="thome"),
    path('adminhome',views.AdminHomeView.as_view(),name="ahome"),
    path('', views.HomeView.as_view(), name="home"),
    path('signupView',views.SignUpView.as_view(),name="signupview"),
    path('SigninView',views.SigninView.as_view(),name="SigninView"),
    path('SignOutView',views.SignOutView.as_view(),name="SignOutView"),
    path('OtpVerificationView',views.OtpVerificationView.as_view(),name="verify"),
    path('accounts/',include('django.contrib.auth.urls')),
]
