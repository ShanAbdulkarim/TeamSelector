# Generated by Django 5.1.2 on 2024-12-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullgame', '0003_teams_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='tradevalue',
            field=models.FloatField(default=0.0),
        ),
    ]
