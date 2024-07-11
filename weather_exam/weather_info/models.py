from django.db import models

# Create your models here.

class Weather(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)
    temperature = models.CharField(max_length=20,null=True,blank=True)
    humidity = models.CharField(max_length=50,null=True,blank=True)
    main = models.CharField(max_length=20,null=True,blank=True)

class History(models.Model):
    country = models.CharField(max_length=30)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.country}"