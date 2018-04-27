# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-27 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=255)),
                ('project_description', models.TextField(default=None)),
                ('proposed_by', models.CharField(default=None, max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('project_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hack.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=255)),
                ('member_name', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='rank',
            name='team_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hack.Team'),
        ),
    ]
