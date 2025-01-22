# Generated by Django 5.1.4 on 2025-01-09 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_profileuser_address'),
        ('utilityapp', '0003_alter_address_created_at_alter_address_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to='utilityapp.address'),
        ),
    ]
