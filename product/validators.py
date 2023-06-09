from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
'''def validate_title(value):
    qs = Product.objects.filter(title__iexact = value)
    print(qs.exists())
    if qs.exists():
        return serializers.ValidationError(f"{value} is already product name")
    print(value)
    return value'''

def validate(value,*args,**kwargs):
    print(args,kwargs,value)
    if "hhh" in value.lower():
        return serializers.ValidationError("is already product name")
    return value


uniqe = UniqueValidator(queryset=Product.objects.all(),lookup="iexact")