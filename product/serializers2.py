from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedRelatedField(
        view_name='product-detail',
        lookup_field = 'pk',
        read_only = True
        )
    username = serializers.CharField(read_only = True)
    pk = serializers.IntegerField(read_only = True)

    
class UserPublicSerializer(serializers.Serializer):
    

        def get_ohter_products(self,obj):
            user = obj
            my_products_qs = user.product_set.all()
            return UserProductInlineSerializer(my_products_qs,many = True,context = self.context).data
