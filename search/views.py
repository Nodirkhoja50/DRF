from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self,*args,**kwargs):
        q = self.request.GET.get('q')
        qs = super().get_queryset(*args,**kwargs)
        user = self.request.user
        if user.is_authenticated:
            user = self.request.user
        result = qs.search(q,user=user)
        return result

    