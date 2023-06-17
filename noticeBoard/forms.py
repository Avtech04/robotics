from django.core import validators
from django import forms
from .models import AdminNotice

class noticeaddition(forms.ModelForm):
    
    class Meta:
        model = AdminNotice
        fields = ['notice']
        widgets = {
            'notice' : forms.Textarea(attrs={'class': 'form-control m-4 p-3 justify-content-center', 'placeholder': 'Enter you Notice here..'}),

        }

    
