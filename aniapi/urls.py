from django.conf.urls import url, include
from aniapi.views import UserViewSet, NewsViewSet, EventViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
