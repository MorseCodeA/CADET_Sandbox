from django import forms
from .models import Document, Json_Model

class DocumentForm(forms.ModelForm):
    """
    Purpose: Form referencing the file being uploaded
    """

    class Meta:
        model = Document
        fields = ('file',)

class JsonForm(forms.ModelForm):
    """
    Purpose: Specifies the 4 form fields in the models.py
    """
    class Meta:
        model = Json_Model
        fields = ['files','comments', 'topics', 'iterations']
