# Generated by Django 3.0.3 on 2020-04-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPS', '0002_auto_20200413_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpsrequest',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
