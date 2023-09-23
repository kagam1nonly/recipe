from django.contrib import admin
from .models import Recipe_app, Ingredient

# Register your models here.
admin.site.register(Recipe_app)
admin.site.register(Ingredient)
