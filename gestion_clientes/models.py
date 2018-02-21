from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from gestion_usuarios import models as modelos_gestion_usuarios
# Create your models here.


class Clientes(modelos_gestion_usuarios.Usuario):
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    fecha_nacimiento = models.DateField(_('Fecha de nacimiento'), null = False)
    numero_identificacion = models.CharField(_('Número de identificación'), max_length=40, null=False)
    direccion = models.CharField(_('Dirección'), max_length=50, blank=False, null=False)

