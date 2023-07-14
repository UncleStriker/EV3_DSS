from rest_framework import viewsets
from paises.api.serializer import PaisesSerializer
from .models import Paises

# Create your views here.


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer
