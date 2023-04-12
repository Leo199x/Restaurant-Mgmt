from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
#from django.contrib.auth.models import User

# Create your models here.



class Restaurant(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=120, default="")
    address = models.CharField(max_length=120,default="")
    description = models.CharField(max_length=128, null=True, blank=True)
    #owner = models.ForeignKey(User, related_name='fff', on_delete=models.CASCADE)
 


