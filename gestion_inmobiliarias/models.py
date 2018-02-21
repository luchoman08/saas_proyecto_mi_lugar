from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from gestion_usuarios import models as gestion_usuarios_models
from gestion_productos import models as gestion_productos_models
# Create your models here.

class Inmobiliaria(models.Model):
    nombre = models.CharField(_('Nombre inmobiliaria'), max_length=100, null = False )
    empleados = models.ManyToManyField(
                                gestion_usuarios_models.Usuario,
                                through='EmpleadoInmobiliaria',
                                through_fields=('inmobiliaria', 'empleado'),
                                related_name='usuariosInscritos')
#productos ?? no se me ocurre

class EmpleadoInmobiliaria(models.Model):
    DIGITADOR = 'DIGITADOR'
    ADMINISTRADOR = 'ADMINISTRADOR'
    CLIENTE = 'CLIENTE'
   
    ROL_VALS = (DIGITADOR, ADMINISTRADOR, CLIENTE)
    ROL_NAMES = (_('Digitador'), _('Administrador'), _('Cliente'))
    ROL_TYPES=   tuple(zip(ROL_VALS, ROL_NAMES))
    inmobiliaria  = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, related_name='inmobiliariaEmpleado')
    empleado = models.ForeignKey(gestion_usuarios_models.Usuario, on_delete = models.CASCADE, related_name = 'empleadoInombiliaria')
    rol = models.CharField(max_length=40, null = False, choices = ROL_TYPES )
    fecha_inicio = models.DateField(_('Fecha de inicio en la inmobiliaria'))
    salario = models.DecimalField(_('Salario del empleado'), null = False, decimal_places = 3, max_digits = 20)
