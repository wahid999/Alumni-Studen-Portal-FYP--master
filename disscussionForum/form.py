from .models import *


class DissFroumForm(forms.ModelForm):

    class Meta:
        model=DissForum
        fields='__all__'
        exclude=['author']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control '
  