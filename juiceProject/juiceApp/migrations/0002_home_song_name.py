# Generated by Django 4.0.4 on 2022-05-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='song_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
