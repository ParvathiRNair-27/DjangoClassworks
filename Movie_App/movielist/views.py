from django.shortcuts import render,redirect
from django.templatetags.i18n import language



# def addmovie(request):
#     return render(request,'addmovie.html')
    #Create your views here.

from movielist.forms import MovieForm
def addmovie(request):
    if request.method=="POST":
        print(request.POST)
        print(request.FILES)
        form_instance = MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            m=Movie.objects.create(movie_name=form_instance.cleaned_data['movie_name'],
                                   description=form_instance.cleaned_data['description'],
                                   director_name=form_instance.cleaned_data['director_name'],
                                   language=form_instance.cleaned_data['language'],
                                   year=form_instance.cleaned_data['year'],
                                   image=form_instance.cleaned_data['image'])
            m.save()
            return redirect('movielist')

    form_instance=MovieForm()
    return render(request, 'addmovie.html',{'form':form_instance})

from movielist.models import Movie
def movielist(request):
    m=Movie.objects.all()
    print(m)
    return render(request,'movielist.html',{'movies':m})

def moviedetail(request,i):
    m=Movie.objects.get(id=i)
    return render(request,'moviedetail.html',{'movie':m})

# delete movie view
def deletemovie(request,i):
    m=Movie.objects.get(id=i)
    m.delete()
    return redirect('movielist')

def editmovie(request,i):
    m=Movie.objects.get(id=i)
    if(request.method=="POST"):
        form_instance=MovieForm(request.POST,request.FILES,instance=m)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('movielist')
    form_instance = MovieForm(instance=m)
    return render(request, 'editmovie.html',{'form':form_instance})

