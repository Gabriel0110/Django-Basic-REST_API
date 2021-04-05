from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, SpellSerializer
from .models import Hero, Spell

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all().order_by('name')
    serializer_class = SpellSerializer