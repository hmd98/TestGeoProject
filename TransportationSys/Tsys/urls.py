from django.urls import path
from .views import RedAndBlue, OwnerRegister
urlpatterns = [
    path('red&blue/', RedAndBlue.as_view()),
    path('owner_register/', OwnerRegister.as_view())
]