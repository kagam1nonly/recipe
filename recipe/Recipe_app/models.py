from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(max_length=255, blank=False, default='')
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)

    def __str__(self):
        return self.name

class Recipe_app(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    ingredient = models.TextField(max_length=255, blank=False, default='')
    procedures = models.TextField(max_length=255, blank=False, default='')

    class Meta:
        ordering = ['created']
