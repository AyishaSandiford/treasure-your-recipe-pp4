from django.shortcuts import render, HttpResponse
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def get_dashboard_view(request):
    # Filter the recipies and show only the ones for the currently logged in user
    # Recipe.objects.filter(user=currently_logged_in_user)
    # request.user.username
    # return HttpResponse(Recipe.objects.all()[0].title)
    # return HttpResponse(request.user.id)
    # return data[0]
    
    currently_logged_in_user_id = request.user.id
    all_recipes = Recipe.objects.all()
    filtered_recipes = all_recipes.filter(user = currently_logged_in_user_id)

    # return HttpResponse(filtered_recipes.all())
    return render(request, "recipe/dashboard/dashboard.html", {"recipes": filtered_recipes.all() })

    

    # return HttpResponse("Nada")
   
