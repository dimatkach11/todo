from django.shortcuts import render

# Create your views here.

# we need to:
# Query the database for all heroes
# Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer