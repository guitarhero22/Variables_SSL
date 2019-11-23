from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        username = request.POST['username']
        password = request.POST['password']
        verify = request.POST['verify']
        email = request.POST['Email']
        if first_name == "" or last_name == "" or username == "" or password == "" or verify == "" or email == "":
            messages.info(request, 'make sure you fill all fields!')
            return render(request, 'register.html')
        elif password == verify:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('home')
        else:
            messages.info(request, 'make sure you verify your password!')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

def home(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
