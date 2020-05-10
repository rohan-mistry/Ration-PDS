# Generated by Django 3.0.3 on 2020-04-12 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ration_id', models.CharField(max_length=15)),
                ('shop_id', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('wheat', models.IntegerField()),
                ('rice', models.IntegerField()),
                ('dal', models.IntegerField()),
                ('kerosene', models.IntegerField()),
                ('custom_id', models.CharField(default='SOME STRING', max_length=15)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
        ),
    ]
