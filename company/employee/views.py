from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
#Employee
# Create your views here.

class ProductView(View):
    def get(self, request):
        return render(request, "products.html")
class AddProduct(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "addpro.html", {"form":form})
    def post(self, request):
        form_data = ProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect("pro")
        else:
            return render(request, "addpro.html", {"form":form_data})


