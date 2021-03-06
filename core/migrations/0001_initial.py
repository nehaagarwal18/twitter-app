# Generated by Django 2.0.1 on 2018-01-20 12:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TweetMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField(unique=True)),
                ('tweet_id_str', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_id_str', models.CharField(blank=True, max_length=50, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('screen_name', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('retweet_count', models.IntegerField(blank=True, null=True)),
                ('favourite_count', models.IntegerField(blank=True, null=True)),
                ('follower_count', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=20, null=True)),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user_mentions', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tweet Metadata',
                'verbose_name_plural': 'Tweets Metadata',
                'db_table': 'tweet_metadata',
            },
        ),
    ]
