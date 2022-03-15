from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET', 'POST'])
def products_list(request):

  if request.method == 'GET':
    products = Product.objects.all()                     
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



    