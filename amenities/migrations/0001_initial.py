# Generated by Django 2.2.3 on 2019-11-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('church', models.CharField(max_length=50)),
            ],
        ),
    ]
