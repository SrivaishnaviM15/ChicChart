from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile=models.IntegerField(default=0000000000)
    address=models.CharField(max_length=100,default='abc')
    email=models.EmailField(default='abc@gmail.com')
    def __str__(self):
        return self.username
    