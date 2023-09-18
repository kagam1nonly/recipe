from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

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

    def put(self, request, pk=None):
        recipe = self.get_object()
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
