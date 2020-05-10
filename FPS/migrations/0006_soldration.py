# Generated by Django 3.0.3 on 2020-04-23 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FPS', '0005_auto_20200418_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldRation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('rationid', models.CharField(max_length=15)),
                ('wheat', models.IntegerField()),
                ('rice', models.IntegerField()),
                ('dal', models.IntegerField()),
                ('kerosene', models.IntegerField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPS.Shop')),
            ],
        ),
    ]