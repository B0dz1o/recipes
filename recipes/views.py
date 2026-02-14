from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Recipe, Tag
from .forms import RecipeUploadForm
import os

# Create your views here.

def recipe_list(request):
    """View to list all recipes with optional tag filtering"""
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    
    # Filter by tags if specified
    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        for tag_id in selected_tags:
            recipes = recipes.filter(tags__id=tag_id)
        recipes = recipes.distinct()
    
    context = {
        'recipes': recipes,
        'tags': tags,
        'selected_tags': [int(t) for t in selected_tags] if selected_tags else [],
    }
    return render(request, 'recipes/recipe_list.html', context)


def recipe_detail(request, pk):
    """View to display a single recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/recipe_detail.html', context)


def recipe_upload(request):
    """View to handle recipe upload"""
    if request.method == 'POST':
        form = RecipeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, f'Recipe "{recipe.title}" uploaded successfully!')
            return redirect('recipe_list')
    else:
        form = RecipeUploadForm()
    
    context = {
        'form': form,
    }
    return render(request, 'recipes/recipe_upload.html', context)


def generate_cookbook(request):
    """Generate a combined LaTeX cookbook from selected recipes"""
    recipes = Recipe.objects.all()
    
    # Filter by tags if specified
    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        for tag_id in selected_tags:
            recipes = recipes.filter(tags__id=tag_id)
        recipes = recipes.distinct()
    
    # Generate LaTeX document
    latex_content = []
    latex_content.append(r'\documentclass{article}')
    latex_content.append(r'\usepackage[utf8]{inputenc}')
    latex_content.append(r'\title{My Cookbook}')
    latex_content.append(r'\author{}')
    latex_content.append(r'\date{}')
    latex_content.append(r'\begin{document}')
    latex_content.append(r'\maketitle')
    latex_content.append(r'\tableofcontents')
    latex_content.append(r'\newpage')
    latex_content.append('')
    
    for recipe in recipes:
        latex_content.append(f'% Recipe: {recipe.title}')
        content = recipe.get_latex_content()
        # Remove document class and preamble if present
        lines = content.split('\n')
        in_document = False
        recipe_lines = []
        for line in lines:
            if r'\begin{document}' in line:
                in_document = True
                continue
            elif r'\end{document}' in line:
                break
            elif in_document:
                recipe_lines.append(line)
        
        if recipe_lines:
            latex_content.extend(recipe_lines)
        else:
            # If no \begin{document} found, include the whole content
            latex_content.append(content)
        
        latex_content.append('')
        latex_content.append(r'\newpage')
        latex_content.append('')
    
    latex_content.append(r'\end{document}')
    
    # Return as downloadable file
    response = HttpResponse('\n'.join(latex_content), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="cookbook.tex"'
    return response

