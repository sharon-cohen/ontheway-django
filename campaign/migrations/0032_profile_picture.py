# Generated by Django 2.2.13 on 2020-07-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0031_auto_20200716_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='', upload_to='campaign/images'),
        ),
    ]
