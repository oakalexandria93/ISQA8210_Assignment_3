# Generated by Django 4.0.2 on 2022-02-23 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    #dependencies = [
    #    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    #    ('pet', '0002_remove_owner_body'),
    #]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
