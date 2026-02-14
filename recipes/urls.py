from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('upload/', views.recipe_upload, name='recipe_upload'),
    path('generate-cookbook/', views.generate_cookbook, name='generate_cookbook'),
]
