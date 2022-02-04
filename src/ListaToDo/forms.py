from django.forms import ModelForm
from django import forms
from .models import Lista
from django.contrib.auth.models import User

class ListaForm(forms.ModelForm):
    
    class Meta:
        model = Lista
        fields = ['name', 'description', 'state', 'date_expire', 'coment']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'date_expire': forms.TextInput(attrs={'class':'form-control'}),
            'coment': forms.Textarea(attrs={'class':'form-control'}),   
        }
    
    