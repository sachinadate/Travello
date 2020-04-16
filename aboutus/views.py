from django.shortcuts import render

# Create your views here.

def about(requset):
    return render(requset,'about.html')