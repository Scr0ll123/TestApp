# Generated by Django 4.0.3 on 2022-03-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTaskApp', '0003_rename_content_books_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autors',
            name='patronymic',
            field=models.CharField(default='-', max_length=30),
        ),
    ]