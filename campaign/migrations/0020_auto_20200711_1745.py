# Generated by Django 2.2.13 on 2020-07-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0019_auto_20200711_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(default=1, max_length=200, null=True),
        ),
    ]
