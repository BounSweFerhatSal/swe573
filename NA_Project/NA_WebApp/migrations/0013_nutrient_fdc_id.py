# Generated by Django 3.0.5 on 2020-06-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NA_WebApp', '0012_auto_20200621_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='FDC_ID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
