# Generated by Django 4.0.2 on 2023-03-23 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extra_project', '0005_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoriesInst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_project.institution')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_project.category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_project.category')),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_project.donation')),
            ],
        ),
    ]
