# Generated by Django 4.1.6 on 2023-02-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.UUIDField(unique=True, verbose_name='Unique code')),
                ('lines', models.PositiveIntegerField(default=50, verbose_name='Number of lines on the grid')),
                ('columns', models.PositiveIntegerField(default=50, verbose_name='Number of columns on the grid')),
                ('alive_cells', models.JSONField(verbose_name='Alive cells')),
                ('game_over', models.BooleanField(default=False, verbose_name='Game over')),
            ],
        ),
    ]