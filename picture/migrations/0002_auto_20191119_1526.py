# Generated by Django 2.2.3 on 2019-11-19 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Picture',
        ),
    ]
