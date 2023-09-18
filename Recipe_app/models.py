from django.db import models

class Recipe_app(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    ingredient = models.TextField(max_length=255, blank=False, default='')
    procedures = models.TextField(max_length=255, blank=False, default='')

    class Meta:
        ordering = ['created']
