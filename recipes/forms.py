from django import forms
from .models import Recipe, Tag


class RecipeUploadForm(forms.ModelForm):
    """Form for uploading LaTeX recipe files"""
    
    class Meta:
        model = Recipe
        fields = ['title', 'latex_file', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe title'}),
            'latex_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.tex'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def clean_latex_file(self):
        """Validate that uploaded file is a .tex file"""
        file = self.cleaned_data.get('latex_file')
        if file:
            if not file.name.endswith('.tex'):
                raise forms.ValidationError('Only .tex files are allowed.')
        return file
