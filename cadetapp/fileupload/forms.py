from django import forms
from .models import Document, Json_Model

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

class JsonForm(forms.ModelForm):

    class Meta:
        model = Json_Model
        fields = ['files','comments', 'topics', 'iterations']
