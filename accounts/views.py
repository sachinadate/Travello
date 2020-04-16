from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def regester(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['user_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            print('username taken')
            return redirect('regester')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            print('email taken')
            return redirect('regester')

        elif(password1==password2):
            if User.objects.filter(username=username).exists():
                print('username taken')
            if User.objects.filter(email=email).exists():
                print('email taken')
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            print('user created sucessfully!!')
        return redirect('/')
    

    else:
        return render(request,'register.html')