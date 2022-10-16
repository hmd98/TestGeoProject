from django.urls import path
from .views import Cars, OwnerRegister, RoadsView, Nodes, TollStations, LocationsAroundToll1
urlpatterns = [
    path('cars/<str:mode>', Cars.as_view()),
    path('owner_register/', OwnerRegister.as_view()),
    path('station1_600/', LocationsAroundToll1.as_view()),
    path('roads/', RoadsView.as_view()),
    path('nodes/', Nodes.as_view()),
    path('toll', TollStations.as_view())
]