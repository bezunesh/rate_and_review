from userreviews.models import Category, Item
from reviews.models import Review
from .serializers import CategorySerialzer, ItemSerializer, ReviewSerializer, URLPatternSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import urls
from django.http import JsonResponse

class CategoryList(generics.ListCreateAPIView):
    """
    List all categories or create a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

    

class CategoryDetail(generics.RetrieveAPIView):
    """
    Retrive, update or delete a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer


class ItemList(generics.ListAPIView):
    """ List all items of a single category """
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(category_id = self.kwargs['category_id'])

class ItemDetail(generics.RetrieveAPIView):
    """ 
    Retreive, add, update or delete an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

class ItemReviews(generics.ListAPIView):
    """
    List, add, update or delete review of an item.
    """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        try:
            item = Item.objects.get(pk=self.kwargs['pk'])
        except Item.DoesNotExist:
            raise Http404
        return item.reviews.all()


@api_view(['GET'])
def apiList(request):
    """
        List of available API endpoints
    """
    serializer = URLPatternSerializer(urls.urlpatterns, many=True)
    return Response(serializer.data)
