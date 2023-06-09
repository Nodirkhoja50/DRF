from rest_framework import viewsets
from .mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer

class ProductVeiwSet(StaffEditorPermissionMixin,viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    