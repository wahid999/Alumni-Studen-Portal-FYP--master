from django.urls import path,include,re_path
from django.conf.urls import url, include

from django.contrib.auth.views import (LogoutView ,
                                       PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView)
from .views import register,home,UpdateUser,UpdatePassword,LoginView

urlpatterns = [
    path('',home, name='home'),
    path('register/',register, name='register'),
    path('update/',UpdateUser,name="update"),
    path('password/',UpdatePassword,name="password"),
    path('login/', LoginView,name='login'),
    path('logout/',LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name= 'reset_password.html'), name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name= 'reset_password_done.html'), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name= 'reset_password_confirm.html'), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete')


    
]
