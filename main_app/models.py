from django.db import models
from django.contrib.auth.models import User

class Soil(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=250)
    img = models.CharField(max_length=500)
    water = models.CharField(max_length=250)
    light = models.CharField(max_length=250)
    temperature = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    soils = models.ManyToManyField(Soil)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
