from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = [
            'user',
            'id'
        ]

    def create(self, validated_data):

        validated_data['user'] = self.context['request'].user

        book = Book.objects.create(**validated_data)
        book.save()

        return book
