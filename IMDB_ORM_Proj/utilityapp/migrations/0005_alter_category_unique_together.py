# Generated by Django 5.1.4 on 2025-01-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilityapp', '0004_alter_awards_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('category_name', 'category_type')},
        ),
    ]
