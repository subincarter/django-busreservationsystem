from django.shortcuts import render
from .form import loginform

# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    myform=loginform
    return render(request,'login.html',{'myform':myform})