from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth import get_user_model
# User=get_user_model()
from .models import User
from .forms import UserRegisterForm
from .forms import UpdateUserForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UpdateUserForm
    model = User
    ordering = ('username',)
    list_display = ( 'username',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password','is_superuser','is_staff','is_active' )}),
    )
    add_fieldsets = (
        (None, {'fields': ('usename', 'email','password', 'password2')}),
    )



admin.site.register(User)