from django.shortcuts import render, HttpResponse
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect

# Create your views here.
@login_required
def get_dashboard_view(request): 
    currently_logged_in_user_id = request.user.id
    all_recipes = Recipe.objects.all()
    filtered_recipes = all_recipes.filter(user = currently_logged_in_user_id)

    # return HttpResponse(filtered_recipes.all())
    return render(request, "recipe/dashboard/dashboard.html", {"recipes": filtered_recipes.all() })

    

def Create(request):
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            form.save()
            return redirect(get_dashboard_view)
    form = forms.RecipeForm()
    form.as_table()
    return render(request, 'recipe/dashboard/create.html', {'form': form})
   
