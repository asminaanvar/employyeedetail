from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bidgely(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    department=models.TextField(max_length=100)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    '''def activities(self):
        qs = self.activity_set.all() # this gets all the child related objects
        for x in qs:
            result = x.subject # here i am just getting one of the fields from the Activities model
            return result'''
    
class MyFileUpload(models.Model):
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    file_name=models.CharField(max_length=50)
    my_file=models.FileField()

    def __str__(self):
        return self.file_name