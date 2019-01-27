# Generated by Django 2.0.2 on 2018-07-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20180709_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capability',
            name='channel',
        ),
        migrations.AddField(
            model_name='capability',
            name='channels',
            field=models.ManyToManyField(to='backend.Channel'),
        ),
        migrations.AddField(
            model_name='rangecap',
            name='scale',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='setcap',
            name='numopts',
            field=models.IntegerField(default=0),
        ),
    ]