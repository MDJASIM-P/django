from django.urls import path
from .views import *

urlpatterns = [
    path("product/", ProductView.as_view(), name= 'pro'),
    path('addproduct/', AddProduct.as_view(), name = 'addpro')
]