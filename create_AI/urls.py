from django.urls import path
from . import views

urlpatterns = [
    path('AI_create/', views.AI_create, name='create_AI'),
    path('your_AI_list/', views.your_AI_list, name='your_AI_list'),
]