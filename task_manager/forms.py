from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-row-input'}),
            'description': forms.Textarea(attrs={'class': 'form-row-input', 'cols': 70, 'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-row-input'}),
            'due_date': forms.DateInput(attrs={'class': 'form-row-input'}),
        }
