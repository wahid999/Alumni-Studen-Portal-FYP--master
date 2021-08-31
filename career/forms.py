from django import forms
from .models import CareerPost
import re
POST_TYPE_CHOICES=[('Internship','Internship'),('Job','Job')]

class CareerForm(forms.ModelForm):

    class Meta:
        model=CareerPost
        fields='__all__'
        exclude=['author']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control '
        self.fields['title'].widget.attrs['id'] = 'title-career'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['postType'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'file-path validate'
        self.fields['image'].required = False

        # self.fields['desired_field_name'].required = False

        # self.fields['careerFile'].widget.attrs['class'] = 'form-control'




        
        