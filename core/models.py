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
     