# Generated by Django 2.2.6 on 2019-10-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musictimeapp', '0008_auto_20191024_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='audio_samples',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
