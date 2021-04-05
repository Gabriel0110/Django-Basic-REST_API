'''
1. Import the Hero model.
2. Import the REST framework serializer
3. Create a new class that links the Hero with its serializer
'''

from rest_framework import serializers
from .models import Hero, Spell

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class SpellSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spell
        fields = ('id', 'name', 'description')