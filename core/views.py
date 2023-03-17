from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products
from django.contrib.auth.models import User
from .serializers import ProductSerializer
from rest_framework import permissions

# Create your views here.

@api_view(['GET'])
def ProductList(request):
    """
        Products List

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = Products.objects.all()
    print("AUTH :", request.auth, "CONTENT TYPE :", request.content_type, "DATA :", request.data)
    final = {
        'res': 'Success',
        'data': list(data.values())
    }
    
    return JsonResponse(final)

class ProductApi(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]
