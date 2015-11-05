from django import forms
from .models import UploadedFile


class UploadPublicForm(forms.ModelForm):
    '''
    Form used to upload public files - which lack group ownership and
    privacy settings.
    '''
    
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']
