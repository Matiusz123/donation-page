# Generated by Django 4.0.2 on 2023-03-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_project', '0002_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
