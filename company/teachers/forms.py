from django import forms
from .models import *

class Std_ModelForm(forms.ModelForm):
    class Meta:
        model = Std_model
        fields = "__all__"