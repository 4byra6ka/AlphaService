from rest_framework import serializers

from main.models import Category


class ListServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
            