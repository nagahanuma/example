from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'hanuma'})
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        user=User.objects.create()
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save();
        print('user created')
        return redirect('/')
        
    else:
        return render(request,'register.html')    