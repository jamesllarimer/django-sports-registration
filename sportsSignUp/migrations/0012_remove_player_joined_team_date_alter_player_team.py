# Generated by Django 5.0.6 on 2024-12-01 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsSignUp', '0011_rename_is_early_registration_registration_is_late_registration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='joined_team_date',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='sportsSignUp.team'),
        ),
    ]
