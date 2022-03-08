from userreviews.models import Category, Item
from reviews.models import Review
from .serializers import CategorySerialzer, ItemSerializer, ReviewSerializer, URLPatternSerializer
from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . import urls
from django.http import JsonResponse

@api_view(['GET'])
def apiList(request):
    """
        List of available API endpoints
    """
    serializer = URLPatternSerializer(urls.urlpatterns, many=True)
    return Response(serializer.data)


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories or create a category
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer


class ItemList(generics.ListCreateAPIView):
    """ 
    List all items of a single category or create an item for a category.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(category_id = self.kwargs['category_id'])


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Retreive, update or delete an item.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemReviews(generics.ListAPIView):
    """
    List reviews of an item.
    """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        try:
            item = Item.objects.get(pk=self.kwargs['pk'])
        except Item.DoesNotExist:
            raise Http404
        return item.reviews.all()
