# Generated by Django 2.1.7 on 2019-03-19 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.TextField(blank=True, null=True)),
                ('time_of_comment', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Published')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.URLField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(related_name='posts', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments_author', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='core.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.ManyToManyField(related_name='comments_vote', to='core.Profile'),
        ),
    ]
