# Generated by Django 2.2.13 on 2020-07-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0026_auto_20200715_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='num_file',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
        ),
    ]
