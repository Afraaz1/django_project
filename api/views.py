from django.shortcuts import render
from rest_framework import generics
from .models import Anime
from .serializers import AnimeSerializer

# Create your views here.


class AnimeView(generics.CreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer 