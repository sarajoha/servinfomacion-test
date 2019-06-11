from geoapi.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nombre', 'apellido', 'direccion', 'latitud', 'longitud', 'estadogeo')
