# Generated by Django 4.0.1 on 2022-06-07 13:31

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
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=30, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Producto')),
                ('nombreProducto', models.CharField(max_length=30, verbose_name='Nombre de Producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio de Producto')),
                ('stockProducto', models.IntegerField(verbose_name='Stock de Producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MiWeb.categoria')),
            ],
        ),
    ]
