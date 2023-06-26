from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from .models import Account
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            username = form.cleaned_data['username']
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
    
            user = Account.objects.create_user(first_name=first_name, last_name= last_name, email=email,password=password, username= username)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'registration successful')
            return redirect('signup')
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form':form})


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return     
