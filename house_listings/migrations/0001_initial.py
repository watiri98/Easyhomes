# Generated by Django 2.2.3 on 2019-11-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('amenities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House_listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=50)),
                ('Amenities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenities.Amenities')),
            ],
        ),
    ]
