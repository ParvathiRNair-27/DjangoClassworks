from django.shortcuts import render,redirect
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from record.models import Employee
from record.forms import addemployeeForm

def home(request):
    e = Employee.objects.all()
    return render(request, 'home.html', {'Employee': e})


def addemployee(request):
    if (request.method=="POST"):
        form_instance=addemployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
    form_instance=addemployeeForm()
    return render(request,'addemployee.html',{'form':form_instance})

def viewemployee(request):
    e=Employee.objects.all()
    print(e)
    return render(request,'detail.html',{'Employee':e})

def employeedetail(request,i):
    e=Employee.objects.get(id=i)
    return render(request,'viewemployee.html',{'Employee':e})

def edit_view(request, i):
    e = Employee.objects.get(id=i)
    if (request.method == 'POST'):
        form_instance = addemployeeForm(request.POST, request.FILES, instance=e)

        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

    form_instance = addemployeeForm(instance=e)
    return render(request, 'editemployee.html', {'form': form_instance})


def deleteemployee(request, i):
    e = Employee.objects.get(id=i)
    e.delete()
    return redirect('home')






