# Generated by Django 3.2.5 on 2021-07-14 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Accesorio',
                'verbose_name_plural': 'Accesorios',
                'db_table': 'accesorio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'marca',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('ano', models.IntegerField(max_length=4)),
                ('motor', models.CharField(max_length=100)),
                ('transmision', models.CharField(max_length=100)),
                ('frenos', models.CharField(max_length=100)),
                ('medidas', models.CharField(max_length=100)),
                ('accesorio', models.ManyToManyField(to='app.Accesorio')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.marca')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'db_table': 'modelo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'tipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(default='-', max_length=200, upload_to='vehiculos')),
                ('precio', models.FloatField()),
                ('color', models.CharField(max_length=50)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.modelo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'db_table': 'vehiculo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='modelo',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo'),
        ),
    ]
