from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripción')
    imagen = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Imagen del producto')
    precio = models.DecimalField(null=True,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nombre

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    