from django.db import models

# Create your models here.
class user(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    phnno=models.IntegerField()
    class Meta:
        db_table="user"

class user3(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table="user3"
class user6(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    class Meta:
        db_table="user6"
