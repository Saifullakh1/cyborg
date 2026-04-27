from django.urls import path
from .views import streams


urlpatterns = [
    path('streams', streams, name='streams')
]