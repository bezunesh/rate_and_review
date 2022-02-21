from rest_framework import serializers
from userreviews.models import Category, Item
from reviews.models import Review
from django.urls.resolvers import URLPattern

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class URLPatternSerializer(serializers.Serializer):
    name = serializers.CharField()
    pattern = serializers.CharField()