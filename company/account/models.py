from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True) 
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # print firstname as object
    def __str__(self):
        return self.firstname