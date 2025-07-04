"""
URL configuration for Movie_App project.

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
from movielist import views
from django.conf.urls.static import static
from django.conf import settings

app_name='Movie_App'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.movielist,name='movielist'),
    path('',views.MovieListView.as_view(),name='movielist'),
    # path('addmovie',views.addmovie,name='addmovie'),
    path('addmovie',views.AddMovieView.as_view(),name='addmovie'),
    # path('moviedetail/<int:i>',views.moviedetail,name='moviedetail'),
    path('moviedetail/<int:pk>',views.MovieDetail.as_view(),name='moviedetail'),
    # path('deletemovie/<int:i>',views.deletemovie,name='deletemovie'),
    path('deletemovie/<int:pk>',views.DeleteMovie.as_view(),name='deletemovie'),
    # path('editmovie/<int:i>',views.editmovie,name='editmovie'),
    path('editmovie/<int:pk>',views.EditMovie.as_view(),name='editmovie'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)