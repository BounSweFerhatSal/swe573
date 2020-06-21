# Generated by Django 3.0.5 on 2020-06-16 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NA_WebApp', '0008_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NA_WebApp.Diseases')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NA_WebApp.Profile')),
            ],
        ),
    ]