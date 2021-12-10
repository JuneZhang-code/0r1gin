from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Homeimage


def home(request):
    homeimages = Homeimage.objects.all()
    return render(request,'Newsletter/home.html',{'homeimages':homeimages})


def betaprogram(request):
    return render(request,'Newsletter/betaprogram.html')

def mentor(request):
    return render(request,'Newsletter/mentor.html')

def designerhome(request):
    return render(request,'Newsletter/designerhome.html')


def aboutus(request):
    return render(request,'Newsletter/aboutus.html')
