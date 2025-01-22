# Generated by Django 5.1.4 on 2025-01-02 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Aandhra', 'Andhra Pradesh'), ('Arunachal', 'Arunachal Pradesh'), ('Aasam', 'Assam'), ('Bihar', 'Bihar'), ('Chattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujrat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal', 'Himachal Pradesh'), ('J&K', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya P', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil N', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar P', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andamn & N', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra & N', 'Dadra and Nagar Haveli and Daman and Diu'), ('Delhi', 'Delhi'), ('Lakshadweep', 'Lakshadweep'), ('Puducherry', 'Puducherry'), ('Ladakh', 'Ladakh')], max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=200)),
                ('category_type', models.CharField(choices=[('crew', 'Crew'), ('music', 'Music'), ('collections', 'Collection'), ('awards', 'Awards'), ('movie', 'Movie'), ('honours', 'Honours'), ('media', 'Media')], max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language_name', models.CharField(choices=[('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('german', 'German'), ('hindi', 'Hindi'), ('marathi', 'Marathi')], max_length=100)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('award_name', models.CharField(choices=[('oscar', 'Oscar'), ('golden_globe', 'Golden Globe'), ('bafta', 'BAFTA'), ('filmfare', 'Filmfare'), ('national_award', 'National Award'), ('IIFA_Awards', 'IIFA Awards'), ('other', 'Other')], max_length=100)),
                ('description', models.TextField()),
                ('establisment_year', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilityapp.category')),
            ],
            options={
                'db_table': 'awards',
            },
        ),
    ]
