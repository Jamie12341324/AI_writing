from django.urls import path
from . import views

urlpatterns = [
    path('AI_writing/', views.AI_writing, name='AI_writing'),
    path('AI_text_list/<int:ai_id>', views.AI_text_list, name='AI_text_list'),
    path('update_AI/<int:ai_id>', views.update_AI, name='update_AI'),
    path('update_AI2/<int:ai_id>/<int:text_id>', views.update_AI2, name='update_AI2'),
    path('text_rename/<int:ai_id>/<int:text_id>', views.text_rename, name='text_rename'),
    path('text_delete/<int:ai_id>/<int:text_id>', views.text_delete, name='text_delete'),
    path('set_times/<int:ai_id>', views.set_times, name='set_times'),
]