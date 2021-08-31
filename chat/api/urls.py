from django.urls import path, re_path,include
from rest_framework import routers
router = routers.DefaultRouter()

from .views import (
    ChatListView,
    ChatDetailView,
    ChatCreateView,
    ChatUpdateView,
    ChatDeleteView,
    ProfileDetailView,
    DeleteChatView
)

app_name = 'chat'

urlpatterns = [

    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view()),
    path('profile/<pk>/',ProfileDetailView.as_view()),
    path('chat/<pk>/',DeleteChatView.as_view())
    
]
