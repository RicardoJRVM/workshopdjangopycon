from django.contrib import admin
from django.urls import path, include
from nombre_proyecto.nombre_aplicacion import urls as libros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(libros_urls))
]
