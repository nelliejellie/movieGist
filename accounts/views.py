from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check password
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'the username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'that email has been used')
                    return redirect('register') 
                else:
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    auth.login(request,user)
                    messages.success(request,'you are logged in')
                    return redirect('index')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    #form logic
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'you are now logged in')
            return redirect('index')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you have successfully logged out')
        return redirect('index')
