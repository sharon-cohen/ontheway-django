# Generated by Django 3.0.7 on 2020-07-08 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaign.Campaign'),
        ),
    ]
