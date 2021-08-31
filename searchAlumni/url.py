from django.urls import path,include
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    path('',searchIndex,name='search'),

]
