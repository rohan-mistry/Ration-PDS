# Generated by Django 3.0.3 on 2020-04-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPS', '0008_auto_20200426_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpsrequest',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
