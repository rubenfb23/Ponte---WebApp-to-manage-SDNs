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
from ponte import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ponte/network/<int:network_id>', views.network, name='network'),
    path('ponte/network/create_network/<str:latitude>,<str:longitude>',
         views.create_network, name='create_network'),
    path('ponte/group/<int:group_id>', views.group, name='group'),
    path('ponte/group/create_group', views.create_group, name='create_group'),
    path('ponte/configuration', views.configuration, name='configuration'),
    path('ponte/anchor/<int:anchor_id>', views.anchor, name='anchor'),
    path('ponte/anchor/create_anchor/<str:latitude>,<str:longitude>',
         views.create_anchor, name='create_anchor'),
]
