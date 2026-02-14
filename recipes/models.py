from django.db import models
import os

# Create your models here.

class Tag(models.Model):
    """Tag model for categorizing recipes (e.g., 'vegan', 'time-consuming')"""
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Recipe(models.Model):
    """Recipe model for storing LaTeX recipe files"""
    title = models.CharField(max_length=200)
    latex_file = models.FileField(upload_to='recipes/')
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipes')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def get_latex_content(self):
        """Read and return the LaTeX file content"""
        if self.latex_file:
            try:
                with open(self.latex_file.path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                return f"Error reading file: {e}"
        return ""

