from django.contrib import admin
from .models import Service, Device, Network, Group, Anchor
# Register your models here.

admin.site.register(Service)
admin.site.register(Device)
admin.site.register(Network)
admin.site.register(Group)
admin.site.register(Anchor)
admin.site.site_header = 'Ponte Administration'
admin.site.site_title = 'Ponte Administration'
admin.site.index_title = 'Ponte Administration'
