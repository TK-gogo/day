from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets

from api.seriallzers import PersonSerializer
from .models import Person

class TestView(APIView):
    def get(self,request):
        return JsonResponse({'name': '极客', 'age': 88})


class PersonViewSet(viewsets.ModelViewSet):
    # 路径
    queryset = Person.objects.all()
    serializer_class = PersonSerializer