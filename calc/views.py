from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request,'home.html',{'name':"sachin"})


def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=request.POST['radio']
    result=val3
    return render(request,'result.html',{'result':result})