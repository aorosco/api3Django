from django.shortcuts import render

from rest_framework import viewsets
from .models import RegistroEntradaSalida
from .serializers import RegistroEntradaSalidaSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegistroEntradaSalidaViewSet(viewsets.ModelViewSet):
    queryset = RegistroEntradaSalida.objects.all()
    serializer_class = RegistroEntradaSalidaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
