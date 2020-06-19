# Generated by Django 3.0.5 on 2020-06-19 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NA_WebApp', '0010_profile_allergies_profile_foodpreferences_profile_restrictedingredients_profile_restrictedlabels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('prepTime', models.IntegerField()),
                ('cookTime', models.IntegerField()),
                ('portions', models.IntegerField()),
                ('instructions', models.CharField(max_length=3000)),
                ('difficulity', models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], null=True)),
                ('totalEnergy', models.DecimalField(decimal_places=10, default=0, max_digits=15, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='calorie',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=15, null=True),
        ),
        migrations.CreateModel(
            name='Recipe_Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Labels')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('energy', models.DecimalField(decimal_places=10, default=0, max_digits=15, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, default=0, max_digits=18, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Ingredient')),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Nutrient')),
            ],
        ),
    ]
