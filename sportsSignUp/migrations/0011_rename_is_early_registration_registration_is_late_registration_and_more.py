# Generated by Django 5.0.6 on 2024-12-01 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsSignUp', '0010_remove_team_team_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='is_early_registration',
            new_name='is_late_registration',
        ),
        migrations.AddField(
            model_name='registration',
            name='division',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='sportsSignUp.division'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='stripe_checkout_session',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], default='pending', max_length=50),
        ),
    ]