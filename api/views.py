from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerialzer, ItemSerializer
from userreviews.models import Category, Item

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerialzer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerialzer(category)
    return Response(serializer.data)

@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getItemsByCategory(request, category_id):
    items = Item.objects.filter(category=category_id)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getItem(request, item_id):
    item = Item.objects.get(id=item_id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

# todo: getReviews for an item
# todo: getRatings for an item

    