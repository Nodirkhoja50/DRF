from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product
from rest_framework.reverse import reverse
from . import validators
from .serializers2 import UserProductInlineSerializer
class ProductSerializer(ModelSerializer):
    
    
    '''url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk'
    )'''

    #email = serializers.EmailField(write_only = True)
    owner = UserProductInlineSerializer(source = 'user',read_only=True)
    title = serializers.CharField(validators=[validators.validate,validators.uniqe])
    #name = serializers.CharField(source='title',read_only = True)
    body = serializers.CharField(source = 'content')
    class Meta:
        model=Product
        fields = [
            'owner',
            'id',
            'url',
            #'name',
            'title',
            'body',
            'price',
            'sale_price',
            'get_absulute_url'
        ]


    ''' def create(self, validated_data):
       email = validated_data.pop('email')
       obj = super().create(validated_data)
       print(email,obj)
       return obj'''
    
    '''def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update",kwargs={"pk":obj.pk},request=request)'''
    

    '''def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
         return None 
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()'''