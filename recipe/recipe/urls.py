from django.contrib import admin
from django.urls import path, include
from Recipe_app.views import index

urlpatterns = [
    path('', index, name='index'),
    path('AllRecipe/', index, name='all-recipes'),
    path('AddRecipe/', index, name='add-recipe'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('recipe_app/', include('Recipe_app.urls'))
    ])),
]
