from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields  = "__all__"
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "man_date":forms.DateInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "exp_date":forms.DateInput(attrs={"class":"form-control", "type":"date"}),
        }