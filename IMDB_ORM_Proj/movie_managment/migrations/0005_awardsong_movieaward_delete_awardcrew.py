# Generated by Django 5.1.4 on 2025-01-03 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_managment', '0004_awardcrew_moviecollection_moviecrew_moviemusic'),
        ('utilityapp', '0002_alter_awards_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('award_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilityapp.awards')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_managment.song')),
            ],
            options={
                'db_table': 'awardsong',
            },
        ),
        migrations.CreateModel(
            name='MovieAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('award_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilityapp.awards')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_managment.movie')),
            ],
            options={
                'db_table': 'movieaward',
            },
        ),
        migrations.DeleteModel(
            name='AwardCrew',
        ),
    ]
