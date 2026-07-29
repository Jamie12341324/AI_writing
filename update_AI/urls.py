from django.urls import path
from . import views

urlpatterns = [
    path('AI_writing/', views.AI_writing, name='AI_writing'),
    path('update_AI/', views.update_AI, name='update_AI'),
]