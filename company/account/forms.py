from django import forms
from .models import *


#  ioc - Inversion Of Control : 
class RegForm(forms.Form):
    first_name = forms.CharField(label="Enter First name" , max_length=100, widget=forms.TextInput(attrs={"placeholder": "Firstname"}), )
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control bg-info"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    age = forms.IntegerField()
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}))
    # overriding of clean() method for customized validation of inputs
    def clean(self):
        pswd = self.cleaned_data.get("password")    # self equals the object where that called with
        if len(pswd) >8 :
            msg = "Password is more than 8 characters"
            self.add_error("password", msg)
            return super().clean()
        
class LogForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    def clean(self):
        pswd = self.cleaned_data.get("password")    # self equals the object where that called with
        if len(pswd) >8 :
            msg = "Password is more than 8 characters"
            self.add_error("password", msg)
            return super().clean()

import re   
class CountForm(forms.Form):
    text = forms.CharField(max_length=100)
    def clean(self):
        txt = self.cleaned_data.get("text") 
        list = re.findall('[0-9!@#$%^&*_+=:;"`~./?<>|\',-]', txt)
        if len(list) != 0:
            msg = "Not only letters"
            self.add_error("text", msg)         
        return super().clean()
    

class Mng_ModelForm(forms.ModelForm):
    class Meta:
        model = Mng_model
        fields = "__all__"  # all fields in Model creates in Form    # ['field_1', 'field_2'] for only show name and std field
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control bg-info"}),
            "age":forms.NumberInput(attrs={"class":"form-control"})
        }


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields = ["first_name","last_name", "email", "username", "password1", "password2"]
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget= forms.PasswordInput())
    