from django.shortcuts import render, redirect, get_object_or_404
from .forms import InitiateForm
from django.db import IntegrityError
from .models import Initiate
from .models import ShippingAddress
from django.http import JsonResponse
import json
import datetime

# Create your views here.

def support(request):
        return render(request,'Initiate/support.html')

def preorder(request):


    return render(request,'Initiate/preorder.html')

def checkout(request):
    return render(request,'Initiate/checkout.html')

def allproject(request):
    return render(request,'Initiate/allproject.html')

def initiate(request):

    if request.method == 'POST':
        form = InitiateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('allproject')
    else:
        form = InitiateForm()
    return render(request, 'Initiate/initiate.html', {'form' :InitiateForm() })


def allproject(request):
    projects = Initiate.objects.all()
    return render(request, 'Initiate/allproject.html', {'projects': projects})

def viewproject(request, project_pk):
    project = get_object_or_404(Initiate, pk=project_pk)
    if request.method == 'GET':
        form = InitiateForm(instance=project)
        return render(request, 'Initiate/viewproject.html', {'project':project, 'form':form})
    else:
        try:
            form = InitiateForm(request.POST, request.FILES,instance=project)
            form.save()
            return redirect('allproject')
        except ValueError:
            return render(request, 'Initiate/viewproject.html', {'project':initiate, 'form':form, 'error':'Bad info'})
