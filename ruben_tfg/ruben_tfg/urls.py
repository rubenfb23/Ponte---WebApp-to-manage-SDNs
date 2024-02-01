"""
URL configuration for ruben_tfg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from ponte import views
from ponte.models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ponte/red/<int:id_red>', views.red, name='red'),
    path('ponte/red/crear_red/<str:latitud>,<str:longitud>',
         views.crear_red, name='crear_red'),
    path('ponte/grupo/<int:id_grupo>', views.grupo, name='grupo'),
    path('ponte/grupo/crear_grupo', views.crear_grupo, name='crear_grupo'),
    path('ponte/configuracion', views.configuracion, name='configuracion'),
    path('ponte/ancla/<int:id_ancla>', views.ancla, name='ancla'),
]
