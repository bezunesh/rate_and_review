from userreviews.models import Category, Item
from reviews.models import Review
from .serializers import CategorySerialzer, ItemSerializer, ReviewSerializer
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryList(mixins.ListModelMixin, 
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    """
    List all categories or create a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryDetail(mixins.RetrieveModelMixin, 
                    generics.GenericAPIView):
    """
    Retrive, update or delete a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ItemList(mixins.ListModelMixin, generics.GenericAPIView):
    """ List all items of a single category """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ItemDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """ 
    Retreive, add, update or delete an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ItemReviews(APIView):
    """ 
    Retrive, add, update of delete item reviews
    """
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404
        reviews = item.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    