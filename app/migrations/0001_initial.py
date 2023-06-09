# Generated by Django 4.1.7 on 2023-03-29 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
    ]
