from django.contrib import admin
from .models import Servicio, Dispositivo, Red, Grupo
# Register your models here.

admin.site.register(Servicio)
admin.site.register(Dispositivo)
admin.site.register(Red)
admin.site.register(Grupo)
