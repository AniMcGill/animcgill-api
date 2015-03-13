from django.contrib.auth.models import User, Group
from aninews.models import NewsItem, EventItem

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'is_staff')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsItem
        fields = ('url', 'title', 'published', 'contents', 'image')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventItem
        fields = ('url', 'title', 'published', 'when', 'where', 'contents', 'image')
