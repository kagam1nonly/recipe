from django.urls import path
from . import views

urlpatterns = [
    # URLs for Recipe_app model
    path('', views.Recipe_app.as_view({'get': 'list', 'post': 'create'}), name='recipe-list-create'),
    path('<int:pk>/', views.Recipe_app.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='recipe-detail'),

    # URLs for Ingredient model
    path('ingredient/', views.IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('ingredient/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
]
