# Generated by Django 4.0.8 on 2023-01-16 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0007_alter_post_options'),
        ('vote', '0003_remove_vote_down_vote_by_remove_vote_up_vote_by_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={},
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='value',
        ),
        migrations.AddField(
            model_name='vote',
            name='down_vote_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='down_vote_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vote',
            name='up_vote_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='up_vote_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='post.post'),
        ),
    ]
