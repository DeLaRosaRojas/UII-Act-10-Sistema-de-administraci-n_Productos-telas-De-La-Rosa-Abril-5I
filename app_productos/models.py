from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return f'Producto: {self.nombre}, Categoria: {self.categoria}'
