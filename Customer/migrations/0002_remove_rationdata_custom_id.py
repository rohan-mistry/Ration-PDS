# Generated by Django 3.0.3 on 2020-04-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rationdata',
            name='custom_id',
        ),
    ]