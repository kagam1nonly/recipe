# Generated by Django 4.2.5 on 2023-09-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_app', '0005_ingredient_remove_recipe_app_ingredient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_app',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe_app',
            name='ingredient',
            field=models.TextField(default='', max_length=255),
        ),
    ]
