from email.policy import EmailPolicy
from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    desc= models.CharField(max_length=30)