from django.db import models
from django.utils import timezone

#Clase que nos permitira almacenar a los usuarios del sistema,
#El nombre de los usuarios sera como el ej: Diego Jiménez Arenas
class Usuario(models.Model):
    idUsuario = models.CharField(primary_key=True, max_length=256)
    contrasennaUsuario = models.CharField(max_length=14)
    nombreUsuario = models.CharField(max_length=25)
    apellidosUsuario = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    miembroStaff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombreUsuario + " " + self.apellidosUsuario

class ListaCompra(models.Model):
    idListaCompra = models.CharField(primary_key=True, max_length=20)
    costoPresupuestado = models.PositiveIntegerField()
    costoReal = models.PositiveIntegerField()

    def __str__(self):
        return self.idListaCompra

class UsuarioListaCompra(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idListaCompra = models.ForeignKey(ListaCompra, on_delete=models.CASCADE)

class Producto(models.Model):
    codigoProducto = models.CharField(primary_key=True, max_length=14)
    nombreProducto = models.CharField(max_length=25)
    notasAdicionales = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreProducto

class ListaCompraProducto(models.Model):
    idListaCompra = models.ForeignKey(ListaCompra, on_delete=models.CASCADE)
    codigoProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    productoComprado = models.BooleanField()
    costoPresupuestado = models.PositiveIntegerField()

class Region(models.Model):
    idRegion = models.PositiveSmallIntegerField(primary_key=True)
    nombreRegion = models.CharField(max_length=64)
    regionOrdinal = models.CharField(max_length=4)

    def __str__(self):
        return self.nombreRegion

class Provincia(models.Model):
    idProvincia = models.PositiveIntegerField(primary_key=True)
    nombreProvincia = models.CharField(max_length=64)
    regionId = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProvincia

class Comuna(models.Model):
    idComuna = models.PositiveIntegerField(primary_key=True)
    nombreComuna = models.CharField(max_length=64)
    idProvincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComuna


class Tienda(models.Model):
    codigoTienda = models.CharField(primary_key=True, max_length=14)
    nombreTienda = models.CharField(max_length=50)
    nombreSucursal = models.CharField(max_length=50, null=True)
    direccionSucursal = models.CharField(max_length=64)
    comunaSucursal = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    regionSucursal = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTienda + " " + self.nombreSucursal

class ProductoTienda(models.Model):
    codigoProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    codigoTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    costoProducto = models.PositiveIntegerField(default=0)