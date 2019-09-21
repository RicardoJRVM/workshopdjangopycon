from django.shortcuts import render
from rest_framework import viewsets

from nombre_proyecto.nombre_aplicacion.models import Libro
from nombre_proyecto.nombre_aplicacion.serializers import LibroSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer