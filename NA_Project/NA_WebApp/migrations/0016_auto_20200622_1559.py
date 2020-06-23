# Generated by Django 3.0.5 on 2020-06-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NA_WebApp', '0015_recipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_ingredients',
            name='portion_name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe_ingredients',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]