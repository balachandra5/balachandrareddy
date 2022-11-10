from django.db import models

# Create your models here.
class employees(models.Model):
    ename=models.CharField(max_length=88)
    eno=models.IntegerField()
    eid=models.IntegerField()
    email=models.CharField(max_length=99)
    
