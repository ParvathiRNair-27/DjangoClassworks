from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def addbook(request):
    return render(request,'addbook.html')

# user defined forms view
from books.models import books
def addbook1(request):
    # after form submittion (post)
    if (request.method=="POST"):
        print(request.POST)
        print(request.FILES)
        # accessing data from submitted form using request.POST
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        g=request.POST['g']
        l=request.POST['l']
        i=request.FILES['i']
        #   creating a new object/records inside model book
        b=books.objects.create(Title=t,Author=a,Price=p,Pages=g,Language=l,Image=i)
        b.save()  #save the records
        return render(request,'addbook1.html')
    # after the get method to read the data
    return render(request, 'addbook1.html')


# viewbooks
def viewbook(request):
    b=books.objects.all()  # read all records from model books.it return query
    print(b)
    return render(request,'viewbook.html',{'books':b})

# built in form
from books.forms import addbookForm
def addbook(request):
    if (request.method == 'POST'): ##after form submission
        print(request.POST)
        print(request.FILES)
        form_instance=addbookForm(request.POST,request.FILES)
        if  form_instance.is_valid():
            # data=form_instance.cleaned_data
            # print(data)
            # t=data['Title']
            # a=data['Author']
            # p=data['Price']
            # g=data['Pages']
            # l=data['Languages']
            # b = books.objects.create(Title=t, Author=a, Price=p, Pages=g, Language=l)
            # b=books.objects.create(Title=form_instance.cleaned_data['Title'],
            #                        Author=form_instance.cleaned_data['Author'],
            #                        Price=form_instance.cleaned_data['Price'],
            #                        Pages=form_instance.cleaned_data['Pages'],
            #                        Language=form_instance.cleaned_data['Language'],
            #                        Image=form_instance.cleaned_data['Image'])
            # b.save()
            form_instance.save()
            # redirect(pathname)
            return redirect('books:viewbook')
        # if (request.method=="GET"):
    form_instance = addbookForm()
    return render(request, 'addbook.html',{'form': form_instance})

# detail
def bookdetail(request,i):
    print(i)
    b=books.objects.get(id=i)
    return render(request,'detail.html',{'books':b})

# editdetail
def editbook(request,i):
    b=books.objects.get(id=i)
    if (request.method == 'POST'):
        form_instance = addbookForm(request.POST, request.FILES,instance=b)

        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbook')

    form_instance=addbookForm(instance=b)
    return render(request,'editbook.html',{'form': form_instance})

# delete
def deletebook(request,i):
    b = books.objects.get(id=i)
    b.delete()
    return redirect('books:viewbook')

#search
from django.db.models import Q
def searchbook(request):
    if(request.method=="POST"):
        data=request.POST['q']
        print(data)
        b=books.objects.filter(Q(Title__contains=data) | Q(Author__contains=data) | Q(Language__contains=data))
        #Filter condition- To read two or more records from a table
        #Q object-To use logical and/or/not syntax in ORM Queries
        # __contains=Django lookups----> value present anywhere ie, if name is Paulo Coelho ifwe search Paulo we will get data if lookup is not used data will notbe found
        # syntax- (fieldname_lookup eg: age__gt,age__lt,title__contains,title_icontains)
        print(b)
        context={'books':b}
        return render(request,'searchbook.html',context)
    return render(request,'searchbook.html')


