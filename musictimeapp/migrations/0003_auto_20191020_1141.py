# Generated by Django 2.2.6 on 2019-10-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musictimeapp', '0002_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.CharField(blank=True, default='../static/musictimeapp/images/default-profile-pic.jpg', max_length=200, null=True),
        ),
    ]
