from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login as signin,authenticate
from ewaste.forms import SignUpForm,PickUpForm
from django.contrib.auth import logout
from .models import General,Specific

def detail(request):
     all_general=General.objects.all() 
     context={'all_general':all_general} 
     return render(request,'ewaste/detail.html',context)
def user(request):
     all_specific=Specific.objects.all() 
     context={'all_specific':all_specific} 
     return render(request,'ewaste/user.html',context)     
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            signin(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'ewaste/signup.html', {'form': form})
def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if  form.is_valid():
            return redirect('ewaste:change_password')
    else:
        form=AuthenticationForm()
    return render(request,'ewaste/login.html',{'form':form})
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
def logout(request):
    if request.method=='POST':
        logout(request)
    return redirect('ewaste:signin')
def index(request):
    return render(request,'ewaste/index.html')
def pick(request):
    if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ewaste:user')
    else:
        form =PickUpForm()
    return render(request, 'ewaste/specific.html', {'form': form})