from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class AI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)