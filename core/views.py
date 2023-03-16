from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products
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
    final = {
        'res': 'Success',
        'data': data.values()
    }
    
    return Response(final)
