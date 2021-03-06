# Generated by Django 2.0.2 on 2018-07-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_auto_20180716_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capability',
            old_name='e_endlabel',
            new_name='eventlabel',
        ),
        migrations.RemoveField(
            model_name='capability',
            name='e_startlabel',
        ),
        migrations.AddField(
            model_name='rule',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='type',
            field=models.CharField(choices=[('es', 'es'), ('ss', 'ss')], default='es', max_length=3),
            preserve_default=False,
        ),
    ]
