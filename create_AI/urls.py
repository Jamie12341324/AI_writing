from django.urls import path
from . import views
from create_AI.views import AI_create2
from create_AI.views import AI_create
from create_AI.views import your_AI_list

urlpatterns = [
    path('AI_create/', AI_create, name='AI_create'),
    path('AI_create2/<int:ai_id>', AI_create2, name='AI_create2'),
    path('your_AI_list/', your_AI_list, name='your_AI_list'),
]