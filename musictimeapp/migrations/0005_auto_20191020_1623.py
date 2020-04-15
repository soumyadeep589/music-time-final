# Generated by Django 2.2.6 on 2019-10-20 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musictimeapp', '0004_auto_20191020_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musictimeapp.Post'),
        ),
    ]
