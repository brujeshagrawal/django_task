# Generated by Django 2.2.7 on 2019-11-28 08:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Indian mobile number', regex='^(\\+\\d{1,3}[- ]?)?\\d{10}$')])),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dob', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]