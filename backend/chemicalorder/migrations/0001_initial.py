# Generated by Django 5.1.6 on 2025-02-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChemicalOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical_name', models.CharField(max_length=255)),
                ('cas_number', models.CharField(max_length=255)),
                ('orderer', models.CharField(max_length=255)),
            ],
        ),
    ]
