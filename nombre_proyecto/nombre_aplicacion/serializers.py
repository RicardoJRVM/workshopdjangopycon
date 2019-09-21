from rest_framework import  serializers
from nombre_proyecto.nombre_aplicacion.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['codigo','autor']