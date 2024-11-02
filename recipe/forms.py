from django import forms
from .models import Recipe


class RecipeForm(forms.ModelsForm):
    class Meta:
        model = Recipe
        fields = ['title','ingredients', 'instructions']