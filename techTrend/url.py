from django.urls import path,include
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('',TechTrendDisplay,name='TechTrendDisplay'),
    path('<int:id>/',TechTrendDisplayDetail,name='TechTrendDisplayDetail'),
    path('add/',AddTechTrend,name='addTechTrend'),
    path('update/<int:id>/',UpdateTechTrend,name='updateTechTrend'),
    path('delete/<int:id>/', DeleteTechTrend, name='deleteTechTrend'),
    path('addComments/', addComments, name='addComments_TechTrend'), 
    path('deleteComments/<int:pk>/<int:id>/', deleteComments, name='deleteCommentsTechTrend'),    
    
    
]
