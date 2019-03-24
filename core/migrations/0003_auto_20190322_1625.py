# Generated by Django 2.1.7 on 2019-03-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190320_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ManyToManyField(related_name='post_votes', to='core.Profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='vote',
            field=models.ManyToManyField(related_name='comment_votes', to='core.Profile'),
        ),
    ]