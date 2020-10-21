"""employee_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from cita.views import *

urlpatterns = [

    path('', welcome),
    path('registro', registro),
    path('login', login),
    path('logout', logout),

    path('admin/', admin.site.urls),

    path('cliente_list', cliente_list, name='cliente_list'),
    path('servicio_list', servicio_list, name='servicio_list'),
    path('empleado_list', empleado_list, name='empleado_list'),
    path('cita_list', cita_list, name='cita_list'),
    # ruta de employee
    path('employee/', include('employee_register.urls')),
    #path('servicio/', include('servicio.urls')),
    path('cliente/', include('cita.urls-cliente')),
    path('cita/', include('cita.urls-cita')),
    path('empleado/', include('cita.urls-empleado')),
    path('servicio/', include('cita.urls-servicio'))
]
