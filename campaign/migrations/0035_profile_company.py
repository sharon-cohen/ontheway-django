# Generated by Django 2.2.13 on 2020-07-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0034_auto_20200719_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
