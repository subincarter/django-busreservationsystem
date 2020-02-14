from django.shortcuts import render
from .form import loginform
from django.http import HttpResponse
from .models import *
from  .forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    return render(request,'login.html')
def signup(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            objsignform=signupform()
            objsignform.name=form.cleaned_data['name']
            objsignform.email=form.cleaned_data['email']
            objsignform.username=form.cleaned_data['username']
            objsignform.password=form.cleaned_data['password']
            objsignform.save()
        return HttpResponse('form saved')
    return render(request,'signup.html',{'form':form})

def login(request):
    getdata=signupform()
    getdata=objects.get('username','password')
    if
        return HttpResponse('authenticated')

