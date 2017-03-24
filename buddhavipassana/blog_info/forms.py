
from django import forms
from .models import Document, Category



class BlogCategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'


class BlogDocumentForm(forms.ModelForm):

    class Meta():
        model = Document
        fields = ('topic', 'document_title','document_url','document_logo')