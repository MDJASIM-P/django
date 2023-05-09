from django.db import models

# Create your models here.

class Std_model(models.Model):
    name = models.CharField(max_length=100)
    std = models.IntegerField(verbose_name="Standard")
    CHOICES =(
        ('A', '1'),     # 1 will display, A will be store
        ('B', '2'),
        ('C', '3')
    )
    div = models.CharField(max_length=100, choices= CHOICES, verbose_name="Division")
    DOJ = models.DateField(help_text='yyyy-mm-dd', verbose_name="date of joining")
    image = models.ImageField(upload_to="Std_pics/")
    cv = models.FileField(upload_to="Std_cvs/", db_column="Resume")

    class Meta:
        db_table = "Students"