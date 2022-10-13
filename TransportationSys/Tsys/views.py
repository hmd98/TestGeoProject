from rest_framework.generics import ListAPIView, CreateAPIView
from django.db.models import Q
from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer
# Create your views here.

class RedAndBlue(ListAPIView):
    model = Car
    serializer_class = CarSerializer
    def get_queryset(self):
        return Car.objects.filter(Q(color = 'blue') | Q(color = 'red'))

class OwnerRegister(CreateAPIView):
    model = Owner
    serializer_class = OwnerSerializer
