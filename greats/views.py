from django.shortcuts import render
from rest_framework import generics
from .models import Artist
from .serializers import ArtistSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer