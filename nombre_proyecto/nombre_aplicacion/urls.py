from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from nombre_proyecto.nombre_aplicacion import views

router = routers.DefaultRouter()
router.register('libros',views.LibroViewSet)

urlpatterns = [
    path('',include(router.urls))
]
