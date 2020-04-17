from django.shortcuts import render,redirect

# Create your views here.

def destinations(request):
    return render(request,'destinations.html')