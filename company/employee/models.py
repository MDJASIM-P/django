from django.db import models
from datetime import date

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    man_date = models.DateField(date.today(), auto_now_add=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="pro_image/", null=True)
    options = (
        ('Food', 'Food'),
        ('Cloath', 'Cloath'),
        ('Cosmetics', 'Cos'),
    )
    category = models.CharField(max_length=100, choices=options)
    exp_date = models.DateField()