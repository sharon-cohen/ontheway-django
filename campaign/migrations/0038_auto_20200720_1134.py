# Generated by Django 2.2.13 on 2020-07-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0037_auto_20200719_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='num_file',
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='campaign\\images\\profile.png', upload_to='campaign/images'),
        ),
    ]