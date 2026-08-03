from django.urls import path
from . import views

urlpatterns = [
    path('AI_writing/', views.AI_writing, name='AI_writing'),
    path('AI_text_list/<int:ai_id>', views.AI_text_list, name='AI_text_list'),
    path('update_AI/<int:ai_id>', views.update_AI, name='update_AI'),
]