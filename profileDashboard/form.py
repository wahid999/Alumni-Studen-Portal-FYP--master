from django.contrib.auth import get_user_model
from django import forms
from .models import *
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=250, required=True, label='',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=250, required=True, label='',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=250, required=True, label='',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=250, required=True, label='',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email',)
    
class ProfileForm(forms.ModelForm):

        class Meta:
          model=Profile
          fields='__all__'
          exclude=['id','user']

        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['firstName'].widget.attrs['class'] = 'form-control '
          self.fields['lastName'].widget.attrs['class'] = 'form-control '
          self.fields['contact'].widget.attrs['class'] = 'form-control '
          self.fields['intro'].widget.attrs['class'] = 'form-control '
          self.fields['intro'].widget.attrs['rows'] =  4
          self.fields['intro'].widget.attrs['placeholder'] = "It will be scence by other Alumni's as your Introduction"

          self.fields['firstName'].required=False
          self.fields['lastName'].required=False
          self.fields['contact'].required=False
          self.fields['alumniType'].required=False
          self.fields['intro'].required = False






