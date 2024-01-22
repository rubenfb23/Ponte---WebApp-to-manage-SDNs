from django.db import models


class Servicio(models.Model):
    id_servicio = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return "#" + self.id_servicio + " " + self.nombre


class Dispositivo(models.Model):
    id_dispositivo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=20)
    localizacion = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    sistema_operativo = models.CharField(max_length=20)
    servicios = models.ManyToManyField(Servicio)
    
    def __str__(self):
        return "#" + self.id_dispositivo + " " + self.nombre + " " + self.localizacion


class Red(models.Model):
    id_red = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.BooleanField()
    ip = models.CharField(max_length=20)
    mascara = models.CharField(max_length=20)
    puerta_enlace = models.CharField(max_length=20)
    dispositivos = models.ManyToManyField(Dispositivo)

    def __str__(self):
        return "#" + self.id_red + " " + self.nombre


class Grupo(models.Model):
    id_grupo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    redes = models.ManyToManyField(Red)

    def __str__(self):
        return "#" + self.id_grupo + " " + self.nombre
