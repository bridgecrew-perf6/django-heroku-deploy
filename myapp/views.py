from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from .models import Autor, LibroEditorial, Editorial
from .serializers import AutorSerializer, LibroSerializer, EditorialSerializer

class LibroListCreateView(generics.ListCreateAPIView):
    queryset = LibroEditorial.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['titulo',]

class LibroRetrieveUpdateDeleteView(generics.ListCreateAPIView):
    queryset = LibroEditorial.objects.all()
    serializer_class = LibroSerializer

class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorRetrieveUpdateDeleteView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorialListCreateView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class EditorialRetrieveUpdateDeleteView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer