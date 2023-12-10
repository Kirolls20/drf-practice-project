from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from product.models import Product

@api_view(['POST'])
def api_home(request, **kwargs):
    # instance = Product.objects.first()  # Use first() to get the first instance
    # data = {} 
    # if instance:
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data= serializer.data
        return Response(data)
    return Response({'message':'Not good data'},status=400)
