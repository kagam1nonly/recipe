from django.contrib import admin
from .models import Recipe_app, Ingredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient', 'procedures')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost')    

# Register your models here.
admin.site.register(Recipe_app, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)