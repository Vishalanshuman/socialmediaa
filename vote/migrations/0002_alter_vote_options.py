# Generated by Django 4.0.8 on 2023-01-16 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ['-post']},
        ),
    ]