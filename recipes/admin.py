from django.contrib import admin
from .models import Recipe, Tag

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'get_tags']
    list_filter = ['tags', 'uploaded_at']
    search_fields = ['title']
    filter_horizontal = ['tags']
    
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'

