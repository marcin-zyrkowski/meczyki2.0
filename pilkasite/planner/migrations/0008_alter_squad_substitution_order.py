# Generated by Django 4.1.3 on 2022-12-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_squad_absent_player_squad_substitution_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='substitution_order',
            field=models.SmallIntegerField(default=0),
        ),
    ]