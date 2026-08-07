from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from create_AI.models import AI
from django.contrib.postgres.fields import ArrayField
class training_text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_saved = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    number = models.IntegerField()
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
class AI_values(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
    name2 = models.CharField(max_length=255)
    number = models.IntegerField()
    value_checks = ArrayField(models.CharField(max_length=255),default=list,blank=True)
    value_answers = ArrayField(models.CharField(max_length=255),default=list,blank=True)
    group = models.IntegerField()