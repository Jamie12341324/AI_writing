from django.contrib import admin

# Register your models here.
from .models import training_text
from .models import ai_values

admin.site.register(training_text)
admin.site.register(ai_values)