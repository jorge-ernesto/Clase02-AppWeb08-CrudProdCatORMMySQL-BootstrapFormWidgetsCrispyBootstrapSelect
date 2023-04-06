
from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(max_length=40)

    class Meta:
        db_table="categoria"

    def __str__(self):
        return self.categoria


class Producto(models.Model):
    descripcion=models.CharField(max_length=60,null=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    fecha=models.DateField(null=False)
    precio=models.FloatField(default=0)
    stock=models.IntegerField(default=0)

    class Meta:
        db_table="producto"
        
    def __str__(self):
        return self.descripcion