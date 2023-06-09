from .models import Product
from django.forms.models import model_to_dict
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework import permissions
from .mixins import StaffEditorPermissionMixin,UserQuerySetMixin

# Create your views here.
'''@api_view(["POST"])
def api_home(request,*args,**kwargs):
    #data = model_to_dict(model_Data)
    #instance = Product.objects.all().order_by("?").first()
    #if instance:
        #data = ProductSerializer(instance).data
        #print(data)
    print(request.data)
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)'''

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    '''
    WE SHOULD CHECK LOOKUP
    '''
    #lookup_view = 


product_detail_api_view = ProductDetailAPIView.as_view()

class ListCreateProductAPIView(UserQuerySetMixin,
                               StaffEditorPermissionMixin,
                               generics.ListCreateAPIView):
    queryset = Product.objects.all()
    '''
    StaffEditorPermissionMixin is gains permission for all users like they check they
    could whatch or not they could add or not etc...
    '''
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content =  serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user,content = content)
    '''def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)

        user = self.request.user
        return qs.filter(user = user)'''

list_create_product_api_view = ListCreateProductAPIView.as_view()

class ListProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    '''
    NOT GONNA USE THIS CLASS
    '''
list_product_api_view = ListProductAPIView.as_view()


@api_view(['GET','POST'])
def everything(request,pk = None,*args,**kwargs):
    
    
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product,pk = pk)
            data = ProductSerializer(obj,many = False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many = True).data
        return Response(data)

    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            content = serializer.validated_data.get('content') or None
            title = serializer.validated_data.get('title')
            if content is None:
                content = title
            serializer.save(content = content)
        return Response({'invlaid':"not good data"},status=400)

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_api_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_delete_api_view = ProductDeleteAPIView.as_view()

class ProductMixin(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView
                   ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
             return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        content = serializer.validated_data.get('content') or None
        title = serializer.validated_data.get('title')

        if content is None:
            content = title
        serializer.save(content=content)

product_mixin_api_view = ProductMixin.as_view()

