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
    
# Create a model
class Mng_model(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_pics", null=True) # upload_to defined the path to store data, null value 

    def __str__(self):
        return self.first_name
    class Meta:
        db_table = "Manager"    # to change Table name in db.lite3
# Do migrations to create table
