# Generated by Django 4.1.6 on 2023-02-23 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_description', models.CharField(max_length=100)),
                ('repaired_date', models.DateField()),
                ('cars', models.ManyToManyField(to='cars.cars')),
            ],
        ),
    ]