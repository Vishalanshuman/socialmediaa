# Generated by Django 4.0.8 on 2023-01-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_vote_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(to='post.vote'),
        ),
    ]
