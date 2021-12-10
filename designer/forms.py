from django import forms
from django.forms import ModelForm
from .models import Designeraccount


class DesigneraccountForm(ModelForm):

    class Meta:
        model = Designeraccount
        fields = ['name', 'collectiondescription','email','logoimage']
