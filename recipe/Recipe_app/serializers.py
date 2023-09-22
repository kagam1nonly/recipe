from rest_framework import serializers
from .models import Recipe_app

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe_app
        fields = '__all__'