# Generated by Django 4.2.16 on 2024-11-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
