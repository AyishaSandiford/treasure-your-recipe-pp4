# Generated by Django 4.2.16 on 2024-11-09 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(help_text='List your ingredients here, separated by commas or new lines', max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(help_text='Step-by-step instructions', max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]