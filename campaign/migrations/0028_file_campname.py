# Generated by Django 2.2.13 on 2020-07-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0027_file_num_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='campName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]