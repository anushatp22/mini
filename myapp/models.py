from django.db import models

class register_tb(models.Model):
    Name = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 20)
    Gender = models.CharField(max_length = 10)
    Phone = models.CharField(max_length = 10)
    Username = models.CharField(max_length = 10)
    Password = models.CharField(max_length = 10)
class image_tb(models.Model):
    File=models.CharField(max_length=20)
    Image=models.FileField()
class country_tb(models.Model):
    Countryname=models.CharField(max_length=20)
class state_tb(models.Model):
    Statename=models.CharField(max_length=20)
    Countryid=models.ForeignKey(country_tb, on_delete=models.CASCADE)
class place_tb(models.Model):
    State=models.ForeignKey(state_tb, on_delete=models.CASCADE)
    Country=models.ForeignKey(country_tb, on_delete=models.CASCADE)
    Place=models.CharField(max_length=20)

class file(models.Model):
    n=models.CharField(max_length=20)
    f=models.FileField()
class reg(models.Model):
    name=models.CharField(max_length=20)
    user=models.CharField(max_length=20)
    pas=models.CharField(max_length=20)# Create your models here.
