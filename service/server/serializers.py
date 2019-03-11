from rest_framework import serializers
from server.models import Person
from server.models import Book

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ( 'id','name', 'age', 'time')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price')