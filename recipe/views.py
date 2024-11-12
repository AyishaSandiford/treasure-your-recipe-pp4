from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect
from django.contrib import messages

"""
    Returns the Authorize user's list of recipes.

    This view returns the dashboard template to the user
    displaying all of the user's created recipes

    Parameters:
    object that represents the client's request.

    Returns:
    HttpResponse: 
    
    """

# Create your views here.
@login_required
def get_dashboard_view(request): 
    currently_logged_in_user_id = request.user.id
    all_recipes = Recipe.objects.all()
    filtered_recipes = all_recipes.filter(user = currently_logged_in_user_id)

    # return HttpResponse(filtered_recipes.all())
    return render(request, "recipe/dashboard/dashboard.html", {"recipes": filtered_recipes.all() })

    
@login_required
def Create(request):
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            form.save()
            messages.success(request, "Recipe " + form.cleaned_data['title'] + " was created successfully.")
            return redirect(get_dashboard_view)
    else:
        form = forms.RecipeForm()
    return render(request, 'recipe/dashboard/create.html', {'form': form})


@login_required
def Edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe " + form.cleaned_data['title'] + " was updated successfully.")
            return redirect(get_dashboard_view)
    else:
        form = forms.RecipeForm(instance=recipe)
    
    return render(request, 'recipe/dashboard/edit.html', {'form':form})
   

@login_required
def Delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    recipe.delete()
    messages.success(request, "Recipe " + recipe.title + " was deleted successfully.")
    return redirect(get_dashboard_view)


def Show(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    return render(request, 'recipe/dashboard/show.html', {'recipe':recipe})