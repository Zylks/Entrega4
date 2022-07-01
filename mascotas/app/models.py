from distutils.command.upload import upload
from django.db import models
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    mensaje = models.CharField(max_length=500)
    
    def __str__ (self):
        return self.nombre