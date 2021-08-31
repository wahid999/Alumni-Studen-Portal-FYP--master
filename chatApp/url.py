
from django.urls import path,include,re_path
from .views import index
# //re_path(r'^(?:.*)/?$', 
urlpatterns = [
    re_path(r'^(?:.*)/?$',index,name='messanger')
]