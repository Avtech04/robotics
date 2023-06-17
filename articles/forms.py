from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','body','slug','thumb']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'thumb': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        