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
class ai_values(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ai = models.ForeignKey(AI, on_delete=models.CASCADE)
    # foreign key from chatgpt
    training_text = models.ForeignKey(
    training_text,
    on_delete=models.CASCADE
)
    name2 = models.CharField(max_length=255)
    number = models.IntegerField()
    # models with arrays from chatgpt
    value_checks = models.JSONField(default=list, blank=True)
    value_answers = models.JSONField(default=list, blank=True)
    group = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    