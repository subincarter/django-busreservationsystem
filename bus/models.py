from django.db import models
from .forms import *
# Create your models here.
class signupform(models.Model):
    name=models.TextField()
    email=models.EmailField()
    username=models.TextField()
    password=models.TextField()