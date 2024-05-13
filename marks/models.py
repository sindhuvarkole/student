from django.db import models

# Create your models here.
class Student(models.Model):
        first_name=models.CharField(max_length=100)
        last_name=models.CharField(max_length=100)
        photo=models.ImageField(upload_to='media')
        marks=models.CharField(max_length=100)
        result=models.CharField(max_length=10,blank=True)
        
        def __str__(self):
           return self.last_name

