# Generated by Django 3.0.3 on 2020-04-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Govt', '0002_auto_20200413_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerregistration',
            name='fire_otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopregistration',
            name='secret_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
