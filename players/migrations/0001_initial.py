# Generated by Django 5.0.6 on 2024-12-15 17:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0001_initial'),
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('parent_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('membership_number', models.CharField(blank=True, max_length=50, null=True)),
                ('is_member', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teams.team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linked_players', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreeAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('membership_number', models.CharField(max_length=100)),
                ('is_member', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('INVITED', 'Invited'), ('JOINED', 'Joined'), ('INACTIVE', 'Inactive')], default='AVAILABLE', max_length=20)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_agents', to='leagues.division')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_agents', to='leagues.league')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_agent_profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'league')},
            },
        ),
    ]