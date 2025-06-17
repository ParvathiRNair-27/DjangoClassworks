from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
#func based
# def home(request):
#     return render(request,'home.html')

#Class based
from django.views import View
class HomeView(View): #View name 1st letter should be capital
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')


#func based
# def addbook(request):
#     return render(request,'addbook.html')

#func based
# def addbook(request):
#     return render(request,'addbook.html')

#func based
# user defined forms view
# from books.models import books
# def addbook1(request):
#     # after form submittion (post)
#     if (request.method=="POST"):
#         # print(request.POST)
#         # print(request.FILES)
#         # accessing data from submitted form using request.POST
#         t=request.POST['t']
#         a=request.POST['a']
#         p=request.POST['p']
#         g=request.POST['g']
#         l=request.POST['l']
#         i=request.FILES['i']
#         #   creating a new object/records inside model book
#         b=books.objects.create(Title=t,Author=a,Price=p,Pages=g,Language=l,Image=i)
#         b.save()  #save the records
#         return render(request,'addbook1.html')
#     # after the get method to read the data
#     return render(request, 'addbook1.html')

#class based
from books.models import books
class AddBook1View(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addbook1.html')

    def post(self,request,*args,**kwargs):
        t = request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        g=request.POST['g']
        l=request.POST['l']
        i=request.FILES['i']
                #   creating a new object/records inside model book
        b=books.objects.create(Title=t,Author=a,Price=p,Pages=g,Language=l,Image=i)
        b.save()  #save the records
        return redirect('books:viewbook')




#func based
# viewbooks
# def viewbook(request):
#     b=books.objects.all()  # read all records from model books.it return query
#     print(b)
#     return render(request,'viewbook.html',{'books':b})

#Class based
class ViewBookView(View):
    def get(self,request,*args,**kwargs):
        b = books.objects.all()
        return render(request, 'viewbook.html', {'books': b})



#funcbased
# built in form
# from books.forms import addbookForm
# def addbook(request):
#     if (request.method == 'POST'): ##after form submission
#         print(request.POST)
#         print(request.FILES)
#         form_instance=addbookForm(request.POST,request.FILES)
#         if  form_instance.is_valid():
#             # data=form_instance.cleaned_data
#             # print(data)
#             # t=data['Title']
#             # a=data['Author']
#             # p=data['Price']
#             # g=data['Pages']
#             # l=data['Languages']
#             # b = books.objects.create(Title=t, Author=a, Price=p, Pages=g, Language=l)
#             # b=books.objects.create(Title=form_instance.cleaned_data['Title'],
#             #                        Author=form_instance.cleaned_data['Author'],
#             #                        Price=form_instance.cleaned_data['Price'],
#             #                        Pages=form_instance.cleaned_data['Pages'],
#             #                        Language=form_instance.cleaned_data['Language'],
#             #                        Image=form_instance.cleaned_data['Image'])
#             # b.save()
#             form_instance.save()
#             # redirect(pathname)
#             return redirect('books:viewbook')
#         # if (request.method=="GET"):
#     form_instance = addbookForm()
#     return render(request, 'addbook.html',{'form': form_instance})

#class based
from books.forms import addbookForm
class AddBookView(View):
    def get(self,request,*args,**kwargs):
        form_instance = addbookForm()
        return render(request, 'addbook.html', {'form': form_instance})

    def post(self, request, *args, **kwargs):
        form_instance = addbookForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:viewbook')



# detail
#func based
# def bookdetail(request,i):
#     print(i)
#     b=books.objects.get(id=i)
#     return render(request,'detail.html',{'books':b})

#classbased
class BookDetailView(View):
    def get(self, request,i):
        b = books.objects.get(id=i)
        return render(request, 'detail.html', {'books': b})



# editdetail
#funcbased
# def editbook(request,i):
#     b=books.objects.get(id=i)
#     if (request.method == 'POST'):
#         form_instance = addbookForm(request.POST, request.FILES,instance=b)
#
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('books:viewbook')
#
#     form_instance=addbookForm(instance=b)
#     return render(request,'editbook.html',{'form': form_instance})

# #class based
class EditBookView(View):
    def get(self, request, i):
        b = books.objects.get(id=i)
        form_instance = addbookForm(instance=b)
        return render(request, 'editbook.html', {'form': form_instance})

    def post(self, request,i):
        b = books.objects.get(id=i)
        form_instance = addbookForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:viewbook')


# delete
#func based
# def deletebook(request,i):
#     b = books.objects.get(id=i)
#     b.delete()
#     return redirect('books:viewbook')

#class based
class DeleteBookView(View):
    def get(self,request,i):
        b = books.objects.get(id=i)
        b.delete()
        return redirect('books:viewbook')

#search
#funcbased
# from django.db.models import Q
# def searchbook(request):
#     if(request.method=="POST"):
#         data=request.POST['q']
#         print(data)
#         b=books.objects.filter(Q(Title__contains=data) | Q(Author__contains=data) | Q(Language__contains=data))
#         #Filter condition- To read two or more records from a table
#         #Q object-To use logical and/or/not syntax in ORM Queries
#         # __contains=Django lookups----> value present anywhere ie, if name is Paulo Coelho ifwe search Paulo we will get data if lookup is not used data will notbe found
#         # syntax- (fieldname_lookup eg: age__gt,age__lt,title__contains,title_icontains)
#         print(b)
#         context={'books':b}
#         return render(request,'searchbook.html',context)
#     return render(request,'searchbook.html')

#class based
from django.db.models import Q
class SearchBookView(View):
    def get(self, request):
        return render(request, 'searchbook.html')

    def post(self, request):
        data = request.POST['q']
        print(data)
        b = books.objects.filter(Q(Title__contains=data) | Q(Author__contains=data) | Q(Language__contains=data))
        print(b)
        context = {'books': b}
        return render(request, 'searchbook.html', context)




