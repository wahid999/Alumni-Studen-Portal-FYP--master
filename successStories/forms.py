from django import forms
from .models import SuccessStories
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class SuccessStoriesForm(forms.ModelForm):
    qoute=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model=SuccessStories
        fields="__all__"
        exclude=['author']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control '
        self.fields['title'].widget.attrs['id'] = 'title-SS'   
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['intro'].widget.attrs['class'] = 'form-control'
        self.fields['qoute'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'file-path validate'
        # self.fields['qoute'].widget = '3'
        # self.fields['postType'].widget.attrs['class'] = 'form-control'
        # self.fields['careerFile'].required = False
        # self.fields['careerFile'].widget.attrs['class'] = 'form-control'
        
        