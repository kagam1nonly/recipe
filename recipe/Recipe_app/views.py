from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer, IngredientSerializer
from django.http import HttpResponse
from .models import Recipe_app, Ingredient
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

def home(request):
    return HttpResponse("Welcome to my Recipes!")

class Recipe_app(ModelViewSet):
    
    serializer_class = RecipeSerializer
    
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            recipe_app = self.serializer_class.Meta.model.objects.get(id=pk)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        Recipe_app = self.serializer_class.Meta.model.objects.get(id=pk)
        serializer = RecipeSerializer(Recipe_app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                recipe_app = self.serializer_class.Meta.model.objects.get(id=pk)
                serializer = RecipeSerializer(recipe_app)
                return Response(serializer.data)
            except self.serializer_class.Meta.model.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # No pk provided, list all recipes.
            recipes = self.serializer_class.Meta.model.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            self.serializer_class.Meta.model.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except self.serializer_class.Meta.model.DoesNotExist:
            return Response(status=status.HTTP_400_NOT_FOUND)
        
class IngredientListCreateView(ListCreateAPIView):
            queryset = Ingredient.objects.all()
            serializer_class = IngredientSerializer

class IngredientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
