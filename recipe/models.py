from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Represents a Recipe in Treasure Your Recipe.

    This model is designed to store and manage
    information regarding your recipes.

    Attributes:
    - user (ForeignKey): ID of the user interacting with the database/recipe
    - title (CharField): The name given to the Recipe.
    - ingredients (TextField): A list of all indregients needed to
    create the dish.
    - instructions (TextField): A Step by Step guide on how to
    create the recipe.
    - created_at (DateTimeField): Indicates when the recipe was created
    - updated_at (DateTimeField): Indicates when the recipe was last
    updated

    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_owner"
    )
    title = models.CharField(max_length=50,)
    ingredients = models.TextField(
        max_length=10000, null=False, blank=False,
        help_text="List your ingredients here," \
        "separated by commas or new lines"
    )
    instructions = models.TextField(max_length=10000, null=False, blank=False,
        help_text="Step-by-step instructions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
