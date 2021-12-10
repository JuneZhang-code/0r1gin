from django.shortcuts import render
from .models import Ambassadorimage


# Create your views here.
def ambassador(request):
    ambassadorimages = Ambassadorimage.objects.all()
    return render(request,'ambassador/ambassador.html',{'ambassadorimages':ambassadorimages})
