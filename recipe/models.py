from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_owner")
    title = models.CharField(max_length=50,)
    ingredients = models.TextField(max_length=10000, null=False, blank=False, help_text="List your ingredients here, separated by commas or new lines")
    instructions = models.TextField(max_length=10000, null=False, blank=False, help_text="Step-by-step instructions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"