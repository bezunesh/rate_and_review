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


class ItemList(mixins.ListModelMixin, 
               generics.GenericAPIView):
    """ List all items of a single category """
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Item.objects.filter(category_id = kwargs['category_id'])
        return self.list(request, *args, **kwargs)

class ItemDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    """ 
    Retreive, add, update or delete an item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ItemReviews(mixins.ListModelMixin, 
                  generics.GenericAPIView):
    """
    List, add, update or delete review of an item.
    """
    serializer_class = ReviewSerializer

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        item = self.get_object(kwargs['pk'])
        self.queryset = item.reviews.all()
        return self.list(request, *args, **kwargs)
    