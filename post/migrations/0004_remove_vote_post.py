# Generated by Django 4.0.8 on 2023-01-16 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_votes_vote_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='post',
        ),
    ]
