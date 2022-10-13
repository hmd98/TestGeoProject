from rest_framework.generics import ListAPIView, CreateAPIView
from django.db.models import Q
from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer
# Create your views here.

class Cars(ListAPIView):
    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        mode = self.kwargs['mode']
        if mode == 'red&blue': query = Car.objects.filter(Q(color = 'blue') | Q(color = 'red'))
        elif mode == 'oldowner': query = Car.objects.filter(owner__age__gt=70)
        else : query = Car.objects.all()
        return  query 

class OwnerRegister(CreateAPIView):
    model = Owner
    serializer_class = OwnerSerializer
