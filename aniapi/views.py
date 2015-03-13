from django.contrib.auth.models import User, Group
from aninews.models import NewsItem, EventItem

from aniapi.serializers import UserSerializer, NewsSerializer, EventSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all()
    serializer_class = NewsSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all()
    serializer_class = EventSerializer
