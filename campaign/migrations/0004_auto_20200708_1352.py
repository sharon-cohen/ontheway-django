# Generated by Django 3.0.7 on 2020-07-08 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_auto_20200708_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]