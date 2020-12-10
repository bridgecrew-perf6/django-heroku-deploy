from rest_framework import serializers
from .models import Autor, LibroEditorial, Editorial

class LibroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LibroEditorial
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editorial
        fields = '__all__'