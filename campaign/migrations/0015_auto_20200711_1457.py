# Generated by Django 2.2.13 on 2020-07-11 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0014_campaign_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='author',
            new_name='user',
        ),
    ]
