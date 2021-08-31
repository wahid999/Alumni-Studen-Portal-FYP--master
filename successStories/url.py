from django.urls import path,include
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('',SuccessStoriesDisplay,name='SuccessStoriesDisplay'),
    path('<int:id>/',SuccessStoriesDisplayDetail,name='SuccessStoriesDisplayDetail'),
    path('add/',AddSuccessStories,name='addSuccessStories'),
    path('update/<int:id>/',UpdateSuccessStories,name='updateSuccessStories'),
    path('delete/<int:id>/', DeleteSuccessStories, name='deleteSuccessStories'),
    path('addComments/', addComments, name='addComments_SuccessStories'),
    path('deleteComments/<int:pk>/<int:id>/', deleteComments, name='deleteCommentsSuccessStories'),

    
]
