from django import forms
from .models import Recipe
from django.core.exceptions import ValidationError

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','ingredients', 'instructions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['ingredients'].widget.attrs['class'] = 'form-control'
        self.fields['instructions'].widget.attrs['class'] = 'form-control'