from django.db import models

# Create your models here.
class history(models.Model):
    title = models.CharField(max_length=64)
    temprature = models.FloatField()
    def __str__(self):
        return f"{self.title} - {self.temprature}°C"