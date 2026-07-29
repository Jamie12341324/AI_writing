from django.urls import path
from . import views

urlpatterns = [
    path('create_AI/', views.create_AI, name='create_AI'),
    path('your_AI_list/', views.your_AI_list, name='your_AI_list'),
]