from rest_framework import serializers
from .models import Artist, Review

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image', 'years_active', 'bio')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('artist', 'author', 'subject', 'body')