from django.urls import path,re_path
from .views import *
urlpatterns = [

    # path('', index, name='index'),
    path('',dashboard,name='dashboard'),
    
    path('createProfile/',createprofile,name='createProfile'), 
    path('updateProfile/',updateProfile,name='updateProfile'), 
    path('getUserDegree/', getUserDegree, name='getUserDegree'),
    
    path('UserDegree/',createUserDegree,name='createUserDegree'), 
    path('UserDegree/<int:pk>/',updateUserDegree,name='updateUserDegree'), 
    path('UserDegree/delete/<int:pk>/', deleteUserDegree, name='deleteUserDegree'),

    path('WorkExp/',createWorkExp,name='createWorkExp'), 
    path('WorkExp/<int:pk>/',updateWorkExp,name='updateWorkExp'), 
    path('WorkExp/delete/<int:pk>/', deleteWorkExp, name='deleteWorkExp'),
    
    re_path(r'^brand/(?P<brand>[-\w]+)/all_json_models/', getDegree, name='getDegree'),
    path('getDegreeByDepartment/', getDegreeByDepartment, name='getDegreeByDepartment'),
    
    path('UserInfo/', UserInfo, name='UserInfo'),

    path('showCareer/', showCareer, name='showCareer'),
    path('showSuccessStories/', showSuccessStories, name='showSuccessStories'),
    path('showMarketTrend/', showMarketTrend, name='showMarketTrend'),
    path('userView/<str:username>/', UserView, name="userView"),
    

] 