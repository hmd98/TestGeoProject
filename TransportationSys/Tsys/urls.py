from django.urls import path
from .views import Cars, OwnerRegister
urlpatterns = [
    path('cars/<str:mode>', Cars.as_view()),
    path('owner_register/', OwnerRegister.as_view())
]