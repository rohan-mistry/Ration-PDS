# Generated by Django 3.0.3 on 2020-04-12 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FPS', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reports',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPS.Shop'),
        ),
        migrations.AddField(
            model_name='fpsrequest',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPS.Shop'),
        ),
    ]