# Generated by Django 5.0.3 on 2024-04-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_recipe_reciperesult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciperesult',
            name='all_list',
        ),
        migrations.RemoveField(
            model_name='reciperesult',
            name='created_at',
        ),
        migrations.AddField(
            model_name='reciperesult',
            name='items',
            field=models.JSONField(blank=True, null=True),
        ),
    ]