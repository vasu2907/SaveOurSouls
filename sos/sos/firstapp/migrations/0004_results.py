# Generated by Django 2.0.7 on 2019-04-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_hospital_location_hospital_opd_hospital_wards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_user', models.CharField(max_length=100)),
                ('username_hospital', models.CharField(max_length=100)),
                ('beds', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=1000, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=150, null=True)),
                ('opd1', models.CharField(max_length=10, null=True)),
                ('opd2', models.CharField(max_length=10, null=True)),
                ('distance', models.DecimalField(decimal_places=100, max_digits=100, null=True)),
                ('time', models.DecimalField(decimal_places=100, max_digits=100, null=True)),
            ],
        ),
    ]
