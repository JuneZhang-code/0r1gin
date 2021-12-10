from django.shortcuts import render, redirect, get_object_or_404
from .models import Designerimage
from .models import Designeraccount
from .forms import DesigneraccountForm
from django.http import JsonResponse
import json
import datetime

def designer(request):
    designerimages = Designerimage.objects.all()
    return render(request,'designer/designer.html',{'designerimages':designerimages})

def createaccount(request):

    if request.method == 'POST':
        form = DesigneraccountForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('tx')
    else:
        form = DesigneraccountForm()
    return render(request, 'designer/createaccount.html', {'form' :DesigneraccountForm() })


def tx(request):
    return render(request,'designer/tx.html')
