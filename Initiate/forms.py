from django import forms
from django.forms import ModelForm
from .models import Initiate


class InitiateForm(ModelForm):

    class Meta:
        model = Initiate
        fields = ['name', 'projectdescription','logoimage','productimage',
        'profilelink','story','goal','productdescription','biddingprice',
        'productquantity']
