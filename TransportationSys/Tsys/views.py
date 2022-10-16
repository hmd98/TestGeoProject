from turtle import width
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView
from django.db.models import Q
from .models import Car, Owner, Roads, AllNodes
from .serializers import CarSerializer, OwnerSerializer, RoadSerializer, AllNodesSeializer
# Create your views here.

class Cars(ListAPIView):
    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        mode = self.kwargs['mode']
        if mode == 'red&blue': query = Car.objects.filter(Q(color = 'blue') | Q(color = 'red'))
        elif mode == 'oldowner': query = Car.objects.filter(owner__age__gt=70)
        elif mode == 'illegaltraffic':
            AllNodes.objects.select_related('car', 'road')
            cars = list(AllNodes.objects.filter(Q(road__width__lt=20) & Q(car__type='big')).distinct('car').values_list('car', flat=True))
            print(cars)
            query = Car.objects.filter(pk__in=cars)
        else : query = Car.objects.all()
        return  query 

class OwnerRegister(CreateAPIView):
    model = Owner
    serializer_class = OwnerSerializer

class Nodes(ListCreateAPIView):
    model = AllNodes
    serializer_class = AllNodesSeializer
    queryset = AllNodes.objects.all()

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
class RoadsView(ListCreateAPIView):
    model = Roads
    serializer_class = RoadSerializer
    queryset = Roads.objects.filter(width__lt=20)
    paginate_by = 5
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

class IllegalTraffic(ListAPIView):
    model = AllNodes
    serializer_class = AllNodesSeializer
    queryset = AllNodes.objects.select_related('car', 'road').filter(Q(road__width__lt=20) & Q(car__type='big')).distinct('car')
