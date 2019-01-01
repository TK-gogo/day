from django.conf.urls import url, include
from .views import TestView, PersonViewSet
from rest_framework.routers import DefaultRouter



touter = DefaultRouter()
touter.register(r'prson',PersonViewSet)

urlpatterns = [

    url(r'^test/$', TestView.as_view()),
    url(r'^', include(touter.urls))
]