from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerialzer
from userreviews.models import Category

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerialzer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)