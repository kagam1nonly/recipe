from django.urls import path, include
from .views import Recipe_app

urlpatterns = [
    path('', Recipe_app.as_view({
        'post': 'post'
    })),
    path('<int:pk>', Recipe_app.as_view({
        'put': 'put',
        'patch': 'patch',
        'delete': 'delete',
        'get': 'get',
    })),
]
