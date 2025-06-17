from django.shortcuts import render

# Create your views here.
def third(request):
    # return HttpResponse("Second Page")
    return render(request,'third.html')

def fourth(request):
    # return HttpResponse("Second Page")
    return render(request,'fourth.html')
