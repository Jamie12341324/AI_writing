from django.urls import path
from . import views
from create_AI.views import AI_create2
from create_AI.views import AI_create
from create_AI.views import your_AI_list
from create_AI.views import AI_delete
from update_AI.views import AI_writing

urlpatterns = [
    path('AI_create/', AI_create, name='AI_create'),
    path('AI_create2/<int:ai_id>', AI_create2, name='AI_create2'),
    path('your_AI_list/', your_AI_list, name='your_AI_list'),
    path('AI_delete/<int:ai_id>', AI_delete, name='AI_delete'),
    path('AI_writing/<int:ai_id>', AI_writing, name='AI_writing'),
]