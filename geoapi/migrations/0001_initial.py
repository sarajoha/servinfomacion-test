# Generated by Django 2.2.2 on 2019-06-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=20)),
                ('longitud', models.FloatField(null=True)),
                ('latitud', models.FloatField(null=True)),
                ('estadogeo', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]
