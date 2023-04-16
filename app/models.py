
from django.db import models

# Create your models here.

class Categoria(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    categoria = models.CharField(max_length=40)

    class Meta:
        db_table = "categoria"  # Especificar el nombre de la tabla que se creara en la migración

    def __str__(self):
        return self.categoria

class Producto(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    descripcion = models.CharField(max_length=60, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = "producto"  # Especificar el nombre de la tabla que se creara en la migración

    def __str__(self):
        return self.descripcion
