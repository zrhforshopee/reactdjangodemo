from django.db import models
import uuid
# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False,null=False) #如果没有这个字段，会有宇哥默认的自增id
    name = models.CharField(max_length=6,null=False)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now=True,null=False)

class Book(models.Model):
    name= models.CharField(max_length=6,null=False)
    price = models.IntegerField()