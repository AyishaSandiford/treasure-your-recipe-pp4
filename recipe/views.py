from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
@login_required
def get_dashboard_view(request):
    """
    Renders the dashboard view with recipes specific to the currently logged-in user.

    This view retrieves all recipes associated with the current user, filters them by the user's ID, 
    and displays them on the dashboard page.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
    HttpResponse: The rendered dashboard HTML template with the filtered list of recipes.

    Note:
    The user must be logged in to access this view.
    """
    currently_logged_in_user_id = request.user.id
    all_recipes = Recipe.objects.all()
    filtered_recipes = all_recipes.filter(user=currently_logged_in_user_id)

    # return HttpResponse(filtered_recipes.all())
    return render(
        request,
        "recipe/dashboard/dashboard.html",
        {"recipes": filtered_recipes.all()}
    )


@login_required
def Create(request):
    """
    Handles the creation of a new recipe for the currently logged-in user.

    If the request method is POST, this view processes the submitted recipe form. 
    If the form is valid, it saves the new recipe with the current user's ID and 
    displays a success message. After successful creation, it redirects the user 
    to the dashboard view. If the request method is not POST, an empty recipe form 
    is displayed.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
    HttpResponse: If the request method is GET, renders the recipe creation template 
                  with an empty form. If the form is submitted and valid (POST), 
                  redirects to the dashboard view after saving the recipe.

    Note:
    The user must be logged in to access this view.
    """
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            form.save()
            messages.success(request, "Recipe " + form.cleaned_data[
                'title'
                    ] + " was created successfully.")
            return redirect(get_dashboard_view)
    else:
        form = forms.RecipeForm()
    return render(request, 'recipe/dashboard/create.html', {'form': form})


@login_required
def Edit(request, recipe_id):
    """
    Handles editing an existing recipe for the currently logged-in user.

    Retrieves the specified recipe by ID if it belongs to the current user. 
    If the request method is POST, this view updates the recipe with the 
    provided form data. If the form is valid, it saves the changes, displays 
    a success message, and redirects to the dashboard view. If the request 
    method is not POST, the recipe form is displayed with the current recipe 
    data for editing.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.
    recipe_id (int): The ID of the recipe to edit.

    Returns:
    HttpResponse: If the request method is GET, renders the recipe edit template with 
                  the current recipe data. If the form is submitted and valid (POST), 
                  redirects to the dashboard view after saving the recipe.

    Note:
    The user must be logged in to access this view.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Recipe "
                + form.cleaned_data['title']
                + " was updated successfully."
            )
            return redirect(get_dashboard_view)
    else:
        form = forms.RecipeForm(instance=recipe)

    return render(request, 'recipe/dashboard/edit.html', {'form': form})


@login_required
def Delete(request, recipe_id):
    """
    Handles the deletion of a recipe for the currently logged-in user.

    Retrieves the specified recipe by ID if it belongs to the current user 
    and deletes it. After successful deletion, a success message is displayed, 
    and the user is redirected to the dashboard view.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.
    recipe_id (int): The ID of the recipe to delete.

    Returns:
    HttpResponse: Redirects to the dashboard view after deleting the recipe.

    Note:
    The user must be logged in to access this view.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    recipe.delete()
    messages.success(
        request, "Recipe " + recipe.title + " was deleted successfully.")
    return redirect(get_dashboard_view)


def Show(request, recipe_id):
    """
    Displays the details of a specific recipe for the currently logged-in user.

    Retrieves the specified recipe by ID if it belongs to the current user and 
    renders it in the recipe detail template.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.
    recipe_id (int): The ID of the recipe to display.

    Returns:
    HttpResponse: Renders the recipe detail template with the selected recipe data.

    Note:
    The user must be logged in to access this view.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, user_id=request.user.id)
    return render(request, 'recipe/dashboard/show.html', {'recipe': recipe})
