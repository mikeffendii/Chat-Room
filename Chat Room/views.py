from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from urllib import request
from .forms import SignUpForm,UserCreationForm

def signup(request):

    if request.method == "GET":
        form = SignUpForm()
        context = {
            "form" : form
        }
        return render(request, "signup.html", context)
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
            
    

def home(request):
    return render(request,'home.html' )
    return HttpResponseRedirect('room.html')



def room(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {
            "form" : form
        }
        return render(request, "room.html", context)
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")

    
