from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from create_AI.models import AI
class training_text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_saved = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)