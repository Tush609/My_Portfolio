from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=120,default='Enter a name!')
    pass