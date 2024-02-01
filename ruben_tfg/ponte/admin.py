from django.contrib import admin
from .models import Servicio, Dispositivo, Red, Grupo, Ancla
# Register your models here.

admin.site.register(Servicio)
admin.site.register(Dispositivo)
admin.site.register(Red)
admin.site.register(Grupo)
admin.site.register(Ancla)
admin.site.site_header = 'Ponte Administration'
admin.site.site_title = 'Ponte Administration'
admin.site.index_title = 'Ponte Administration'
