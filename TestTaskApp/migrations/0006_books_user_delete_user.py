# Generated by Django 4.0.3 on 2022-03-21 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TestTaskApp', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
