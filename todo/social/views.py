from django.shortcuts import render

# Create your views here.
# we need to:
# Query the database for all users
# Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered

from rest_framework import viewsets

from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #.order_by('first_name')
    serializer_class = ProfileSerializer