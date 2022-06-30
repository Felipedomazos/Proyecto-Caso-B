from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria =models.CharField(max_length=30, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto =models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    categoria =models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombreProducto =models.CharField(max_length=70, verbose_name='Nombre de Producto')
    precioProducto =models.IntegerField(verbose_name='Precio de Producto')
    stockProducto =models.IntegerField(verbose_name='Stock de Producto')
    imagenProducto =models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombreProducto
    

    