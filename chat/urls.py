from django.urls import path
from chat import views

urlpatterns = [
    path('chat/<str:group_name>/', views.chat),
    
]

