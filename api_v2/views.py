import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from userreviews.models import Category


@api_view(['GET'])
def listCategories(request):
    serializer = CategorySerializer(Category.objects.all(), many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=JSONParser().parse(request))
    if serializer.is_valid():
        serializer.save()
        return Response({'result' : 'success'})
    return Response({'errors': serializer.errors}) 
