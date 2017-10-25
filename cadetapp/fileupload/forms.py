from django import forms
from fileupload.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)
