from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

# Create your models here.

from django.contrib.auth.models import User

class Usuario(User):
    imagen = models.ImageField(_('Imagen de perfil'), null=False, default=0, upload_to='static/imagenes/usuarios')
    estadoHabilitado = models.BooleanField(default=True, null=False)