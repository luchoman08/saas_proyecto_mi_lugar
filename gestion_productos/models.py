from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from gestion_inmobiliarias import models as gestion_inmobiliarias_models

# Create your models here.



# Solamente es un inicio, por favor completar

class Producto(models.Model):
    nombre = models.CharField(_('Nombre de el producto'), max_length=50, null = False)
    estrato = models.PositiveIntegerFiel(_('Estrato'), null= False) 
    direccion = models.CharField(_('Dirección'), max_length= 50, null= False)
    ciudad = models.CharField(_('Ciudad'), max_length= 50, null= False)
    area = models.CharField(_('Área'), max_length= 30, null= False)
    #imagen = models.ImageField(_('Imagen de perfil'), null=False, default=0, upload_to='static/imagenes/productos')
    descripcion = models.CharField(_('Descripción'), max_length= 1000, null= False)
    #antiguedad = model.CharField(_('Antigüedad'), max_length= 50, null= False)

class Servicio(models.Model):
    precio_mensual =  models.DecimalField(_('Precio alquiler'), null = False, decimal_places = 3, max_digits = 20)

class ServicioTiempoDefinido(Servicio):
    fecha_inicio_prestacion = models.DateField(_('Fecha inicio'), null = False, auto_now_add = True)
    tiempo_contratado_dias = models.IntegerField(_('Número de dias contratado'), null = False)

class Apartamento(Producto):
    tiene_garaje = models.BooleanField(_('Garaje incluido'), null = False)
    numero_habitaciones = models.IntegerField(_('Número de habitaciones'), null = False)
    numero_banos = models.PositiveIntegerFiel(_('Número de baños'), null= False)

class Lote(Producto):
    metros_cuadrados =  models.DecimalField(_('Metros cuadrados'), null = False, decimal_places = 3, max_digits = 20)
    #precio terreno
    #tiene_servicios

class OfertaApartamentoAlquilerTiempoDefinido(ServicioTiempoDefinido):
    apartamento = models.ForeignKey(Apartamento, related_name='ofertaAlquilerApartamentoTiempoDefinido', on_delete=models.CASCADE)

class Venta(models.Model):
    producto = models.ForeignKey(Producto, related_name='ventaProducto', on_delete=models.CASCADE)
    #cliente
    #precio venta (no neceariamente el mismo de el producto)


class Casa(Producto):
    numero_habitaciones = models.IntegerField(_('Número de habitaciones'), null = False)
    tiene_garaje = models.BooleanField(_('Garaje incluido'), null = False)
    tiene_patio = models.BooleanField(_('Patio'), null= False) # Toca definir
    numero_banos = models.PositiveIntegerFiel(_('Número de baños'), null= False)

