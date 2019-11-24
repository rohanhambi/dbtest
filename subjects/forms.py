from django.forms import ModelForm
from django import forms
from .models import Subject, SubjectCombination

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code','subject_credits','subject_grade','subject_semester']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code':  forms.NumberInput(attrs={'class': 'form-control'}),
            'subject_credits':  forms.NumberInput(attrs={'class': 'form-control'}),
            'subject_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_semester': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubjectCombinationForm(ModelForm):
    class Meta:
        model = SubjectCombination
        fields = ['select_class', 'select_subject']
        widgets = {
            'select_class': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'select_subject':  forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),           
        }