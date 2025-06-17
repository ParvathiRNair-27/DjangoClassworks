"""
URL configuration for Library project.

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
from django.urls import path
from Books import views
app_name='Books'
urlpatterns = [

    path('',views.home,name="home"),           #http:127.0.0.1:8000
    path('addbook',views.addbook,name="addbook"),
    path('addbook1',views.addbook1,name="addbook1"),#http:127.0.0.1:8000/addbook
    path('viewbook',views.viewbook,name="viewbook"),#http:127.0.0.1:8000/viewbook
    path('bookdetail/<int:i>',views.bookdetail,name="bookdetail"),
    path('editbook',views.editbook,name="editbook"),

]
