from django.db import models

# Create your models here.
class place(models.Model):
    img=models.ImageField(upload_to='design/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)

class team(models.Model):
    img = models.ImageField(upload_to='design/img', null=True, blank=True)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
