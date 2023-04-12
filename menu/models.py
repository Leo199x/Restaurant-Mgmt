from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    price = models.IntegerField(blank=False)
    description = models.CharField(max_length=120, null=True, blank=True)




