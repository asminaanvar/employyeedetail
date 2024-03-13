from django.shortcuts import render,redirect,get_object_or_404
from .models import Bidgely,MyFileUpload
from .forms import Bidgelyform,Uploadform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
import os
import logging
# Create your views here.

def logoutPage(request):
    logout(request)
    return redirect('index')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")


    context={'page':page}
    return render(request,'base/login-register.html',context)

def registerUser(request):
    form= UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        
    else:
         messages.error(request, "An error occured during registration")

    context={'form':form}
    return render(request,'base/login-register.html',context)

def index(request):
    context={}
    return render(request,'base/index.html',context)

@login_required(login_url='loginpage')
def home(request):
    bidgely = Bidgely.objects.all()
    
    context={'Bidgely':bidgely}
    return render(request,'base/home.html',context)


@login_required(login_url='loginpage')
def createfile(request):
    
    form=Uploadform(request.POST or None, request.FILES or None, initial={'owner': request.user})
    print('Logged-in user:', request.user)  # Debugging print to check the logged-in use
    if request.user.is_superuser:
        mydata=MyFileUpload.objects.all()
    else:
        mydata=MyFileUpload.objects.filter(owner=request.user)
    print('Files associated with user:', mydata)  # Debugging print to check the files associated with the user
  
    
    context={'form':form,'mydata': mydata}
    return render (request,'base/createfile.html',context)

def uploadfile(request):
    print('Logged-in user:', request.user)  # Debugging print to check the logged-in user
    
    if request.method=='POST':
        form=Uploadform(request.POST,request.FILES)
        if form.is_valid():
            File_name=request.POST.get('file_name')
            File=request.FILES.get('file')

            exists=MyFileUpload.objects.filter(my_file=File).exists()
            if exists:
                messages.error(request,f'The file {File} is already exists...!!!')
            else:
                mydata=MyFileUpload.objects.create(file_name=File_name,my_file=File,owner=request.user)# Assign the owner field to the logged-in user
                mydata.save()
                messages.success(request, "File Uploaded successfuly")
        return redirect('createfile')
    
    
    
def deleteFile(request,pk):
    mydata = get_object_or_404(MyFileUpload, id=pk)
    file_path = mydata.my_file.path    
    mydata.delete()    
    os.remove(file_path)
    messages.success(request,'File deleted successfully.')  
    return redirect('createfile')
 
def view(request,id):
    bidgely=Bidgely.objects.get(pk=id)
    return  redirect('home')

@login_required(login_url='loginpage')
def add(request):
    
    if request.method == "POST":
        form = Bidgelyform(request.POST)
        if form.is_valid():
            record=form.save(commit=False)
            record.user=request.user
            record.save()
            context = {'form': form, 'success': True}
            return render(request, 'base/add.html', context)
    else:

        user=get_user(request)
        form=Bidgelyform(initial={'user':user,'name':user})
        context = {'form': form, 'success': False}
        return render(request, 'base/add.html', context)

@login_required(login_url='loginpage')
def edit(request,pk):
    if request.method=='POST':
        bidgely=Bidgely.objects.get(id=pk)
        form=Bidgelyform(request.POST,instance=bidgely)
        if form.is_valid():
            form.save()
    
            context={'form':form,'success':True}
            return render(request,'base/edit.html',context)
    
    else:
        bidgely=Bidgely.objects.get(id=pk)
        form=Bidgelyform(instance=bidgely)
        context={'form':form}
        return render(request,'base/edit.html',context)   

@login_required(login_url='loginpage')
def delete(request,pk):
    if request.method=='POST':
        bidgely=Bidgely.objects.get(id=pk)
        bidgely.delete()
        return redirect('home')