from rest_framework import serializers
from .models import Recipe_app, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe_app
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
