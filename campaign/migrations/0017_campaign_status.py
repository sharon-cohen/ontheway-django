# Generated by Django 2.2.13 on 2020-07-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0016_auto_20200711_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('process', 'process'), ('done', 'done'), ('wait', 'wait'), ('running', 'running')], default='wait', max_length=30),
        ),
    ]
