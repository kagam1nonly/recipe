from django.urls import path, include
from .views import Recipe_app

urlpatterns = [
    path('', Recipe_app.as_view({
        'get': 'list',
        'post': 'post'
    })),
    path('<int:pk>/', Recipe_app.as_view({
        'put': 'update'
    })),
]
