# Generated by Django 4.1.3 on 2022-11-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_alter_squad_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]