# Generated by Django 2.2.13 on 2020-07-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0010_auto_20200709_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[(0, 'process'), (1, 'done'), (2, 'wait')], default='wait', max_length=20),
        ),
    ]
