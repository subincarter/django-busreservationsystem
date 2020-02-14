from django.shortcuts import render,redirect
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
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                objlogin = signupform.objects.get(username=username,password=password)
                request.session['user']=objlogin.username
                return render(request,"reserve.html")
            except:
                return redirect('loginpage')
    return render(request,'login.html',{'form':form})



