# Generated by Django 4.0.8 on 2023-01-16 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_post_votes_delete_vote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date']},
        ),
    ]