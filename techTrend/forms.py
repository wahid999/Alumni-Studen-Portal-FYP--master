from django import forms
from .models import TechTrend
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TechTrendForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model=TechTrend
        fields="__all__"
        exclude=['author']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control '
        self.fields['title'].widget.attrs['id'] = 'title-tech'   
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['intro'].widget.attrs['class'] = 'form-control'
        
     