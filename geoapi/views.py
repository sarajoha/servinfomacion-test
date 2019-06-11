from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
import googlemaps
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns a list of users
    Allos creation user object when authenticated
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGeoCode(viewsets.ModelViewSet):
    """
    API endpoint returns list of users without geocoded address
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = User.objects.filter(estadogeo=False)

    serializer = UserSerializer(queryset, many=True)
    
    # gmaps = googlemaps.Client(key='Add Your Key here')

    # Geocoding an address
    # geocode_result = gmaps.geocode(serializer.data.direccion)

    #Save lat and long in user obj
    # serializer.data.longitud = geocode_result[0]
    # serializers.data.latitud = geocode_result[1]
    #sarializar save
