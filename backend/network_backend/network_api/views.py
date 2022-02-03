from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView

# Create your views here.

class PersonAPIView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
