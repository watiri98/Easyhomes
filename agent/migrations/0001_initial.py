# Generated by Django 2.2.3 on 2019-11-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=20)),
                ('Phone_number', models.CharField(max_length=15)),
                ('Agency_name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100)),
                ('Reg_no', models.CharField(max_length=15)),
            ],
        ),
    ]
