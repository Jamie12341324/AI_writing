from django.contrib import admin

# Register your models here.
from .models import training_text
from .models import ai_values
from .models import times_group

admin.site.register(training_text)
admin.site.register(ai_values)
admin.site.register(times_group)