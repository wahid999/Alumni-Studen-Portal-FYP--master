from .views import *
from django.urls import path,re_path

urlpatterns = [

    path('',dissForumHome,name='dissForumHome'),
    path('add',addDissForum,name='addDissForum'),
    path('detail/<int:pk>/', dissForumDetail, name='dissForumDetail'),
    path('delete/<int:pk>/', dissForumDelete, name='dissForumDelete'),
    path('update/<int:pk>/', dissUpdate, name='dissUpdate'),
    path('addComments/', addComments, name='addCommentsDissForum'),
    path('deleteComments/<int:pk>/<int:id>/', deleteComments, name='deleteComments'),
    
    
    
]