from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, ItemSerializer
from userreviews.models import Category, Item

@api_view(['GET', 'POST'])
def categories(request, pk=None):
    """
    List all categories or retreive one category or create a category
    """
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Category, pk=pk)
            serializer = CategorySerializer(obj)
        else:    
            serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data)
    else:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})


@api_view(['GET', 'POST'])
def items(request, pk=None):
    """ 
    List items or retrive an item or add a new item
    """
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Item, pk=pk)
            serializer = ItemSerializer(obj)
        else:
            serializer = ItemSerializer(Item.objects.all(), many=True)
        return Response(serializer.data)
    else:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})