from django.urls import path, include
from .views import ProductList, ProductApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product_api', ProductApi)

urlpatterns = [
    path('', include(router.urls)),
    path('products',ProductList)
]