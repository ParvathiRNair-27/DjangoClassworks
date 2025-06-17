from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

# def addbook(request):
#     return render(request,'addbook.html')
# ##user defined
from Books.models  import Books
def addbook1(request):
    if (request.method == "POST"):  ##after form submission
        print(request.POST)
        print(request.FILES)
        t=request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pg= request.POST['pg']
        l = request.POST['l']
        i=request.FILES['i']
        b=Books.objects.create(Title=t,Author=a,Price=p,Pages=pg,Language=l,Image=i)
        b.save()
        return render(request, 'addbook1.html')
    return render(request,'addbook1.html')


def viewbook(request):
    b = Book.objects.all()
    print(b)
    return render(request,'viewbook.html',{'Books':b})


##built in

from Books.forms import addbookForm
def addbook(request):
    if (request.method == "POST"):
        ##after form submission
        # print(request.POST)
        # print(request.FILES)
        form_instance=addbookForm(request.POST,request.FILES)
        if form_instance.is_valid():
        #     # data=form_instance.cleaned_data
            # t = request.POST['t']
            # a = request.POST['a']
            # p = request.POST['p']
            # pg = request.POST['pg']
            # l = request.POST['l']
            # b = Books.objects.create(Title=t, Author=a, Price=p, Pages=pg, Language=l)
            # b=Books.objects.create(Title=form_instance.cleaned_data['Title'],
            #                         Author =form_instance.cleaned_data['Author'],
            #                        Price=form_instance.cleaned_data['Price'],
            #                        Pages=form_instance.cleaned_data['Pages'],
            #                        Language=form_instance.cleaned_data['Language'],
            #                        Image=form_instance.cleaned_data['Image'])
            #
            # b.save()
            form_instance.save()
            #redirect(pathname)
        return redirect('Books:home')

    form_instance = addbookForm()
    return render(request, 'addbook.html', {'form': form_instance})


#detail view
def bookdetail(request,i):
    print(i)
    b=Book.objects.get(id=i)
    return render(request,'detail.html',{'Books':b})

#Edit view
def editbook(request):
    return render(request,'editbook.html')