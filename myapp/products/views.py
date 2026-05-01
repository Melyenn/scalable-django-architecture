import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

SERVER_ID = os.getenv("APP_NAME", "unknown")


class ProductListCreateView(APIView):
    """
    POST /products 
    """
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "error": serializer.errors,
                    "processed_by": SERVER_ID,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        product = serializer.save()

        return Response(
            {
                "success": True,
                "data": ProductSerializer(product).data,
                "processed_by": SERVER_ID,
            },
            status=status.HTTP_201_CREATED,
        )
    
    """
    GET  /products
    """
    def get(self, request):
        products = Product.objects.all().order_by("-created_at")
        serializer = ProductSerializer(products, many=True)

        return Response(
            {
                "success": True,
                "data": serializer.data,
                "processed_by": SERVER_ID,
            }
        )
