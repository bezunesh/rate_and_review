from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CategorySerialzer, ItemSerializer, ReviewSerializer
from userreviews.models import Category, Item
from reviews.models import Review
from django.http import Http404

class CategoryList(APIView):
    """
    List all categories or create a category
    """
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerialzer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
    Retrive, update or delete a category
    """
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404
        serializer = CategorySerialzer(category)
        return Response(serializer.data)


class ItemList(APIView):
    """ List all items of a single category """
    def get(self, request, category_id):
        items = Item.objects.filter(category=category_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


def getItemByPk(pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

class ItemDetail(APIView):
    """ 
    Retreive, add, update or delete an item.
    """
    def get(self, request, item_id):
        item = getItemByPk(tem_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    
class ItemReviews(APIView):
    """ 
    Retrive, add, update of delete item reviews
    """
    def get(self, request, item_id):
        item = getItemByPk(item_id)
        reviews = item.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    