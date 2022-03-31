from tabnanny import verbose
from django.db import models


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    matni = models.TextField()
    daromadi = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

class EV(models.Model):
    country = models.CharField(max_length=20)
    ev_qty = models.IntegerField()

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Davlat"
        verbose_name_plural = "Davlatlar"

class BEV(models.Model):
    bev_country = models.ForeignKey(EV, on_delete=models.CASCADE, related_name="mamlakat")
    year = models.DateField()
    ownership = models.IntegerField()

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Davlat xalqi"
        verbose_name_plural = "Davlatlar xalqlari"
     