from datetime import datetime
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from django.db.models import Q
from .models import Car, Owner, Roads, AllNodes, TollStation
from .serializers import CarSerializer, OwnerSerializer, RoadSerializer, AllNodesSeializer, TollStationSerializer
from django.contrib.gis.measure import D
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

class RoadsView(ListCreateAPIView): #just to import and test data
    model = Roads
    serializer_class = RoadSerializer
    queryset = Roads.objects.filter(width__lt=20)
    paginate_by = 5
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class LocationsAroundToll1(ListAPIView):
    model = AllNodes
    serializer_class = AllNodesSeializer
    station1 = TollStation.objects.get(name='عوراضی 1').location
    queryset = AllNodes.objects.filter(Q(location__distance_lt=(station1, D(m=600))) & Q(car__type='small'))#& Q(date=datetime.now()) when proper data exict

class TollStations(ListCreateAPIView):
    model = TollStation
    serializer_class = TollStationSerializer
    queryset = TollStation.objects.all()
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

