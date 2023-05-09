from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
# Create your views here.



class Std(View):
    def get(self, request, *args, **kwargs):
        data = Std_model.objects.all()
        return render(request, "home_std.html", {"data":data})

class Std_Reg(View):
    def get(self, request, *args, **kwargs):
        form = Std_ModelForm()
        return render(request, "reg_std.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = Std_ModelForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            print(form_data.cleaned_data)
            messages.success(request, "You are registered Succesfully.Check table to view ur details.")
            return redirect("std")
        else:
            return render(request, "reg_std.html", {"form":form_data})

class Std_Update(View):
    def get(self, request, *args, **kwargs):
        sid = kwargs.get("sid")
        std = Std_model.objects.get(id=sid)
        name =  std.name
        form = Std_ModelForm(instance=std)
        return render(request, "update_std.html", {"form":form, "name":name})
    def post(self, request, *args, **kwargs):
        sid = kwargs.get("sid")
        std = Std_model.objects.get(id=sid)
        form_data = Std_ModelForm(data=request.POST, files=request.FILES, instance=std)
        if form_data.is_valid():
            form_data.save()
            return redirect("std")
        else:
            return render(request, "reg_std.html", {"form":form_data})

class Std_Delete(View):
    def get(self, request, *args, **kwargs):
        sid = kwargs.get("sid")   
        std = Std_model.objects.get(id=sid)
        std.delete()
        messages.success(request, "Student %s Deleted"%std.name)
        return redirect("std")