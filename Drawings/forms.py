from django import forms
from .models import AllDrawing

class AllDrawingForm(forms.ModelForm):
    class Meta:
        model = AllDrawing
        fields = ['name', 'image', 'type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input w-full'}),
            'type': forms.Select(attrs={'class': 'form-select w-full'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea w-full'}),
        }
