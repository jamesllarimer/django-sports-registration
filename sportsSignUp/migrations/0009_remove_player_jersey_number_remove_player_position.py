# Generated by Django 5.0.6 on 2024-11-30 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsSignUp', '0008_alter_player_membership_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='jersey_number',
        ),
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
    ]
