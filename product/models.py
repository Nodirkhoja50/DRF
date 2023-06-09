from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.db.models import Q
User = settings.AUTH_USER_MODEL
# Create your models here

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self,query,user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if qs is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = qs.filter(user=user)
            qs = (qs | qs2).distinct()
        return qs
        

class ProductManager(models.Manager):

    def get_queryset(self,*args,**kwargs):
        return ProductQuerySet(self.model,using=self._db)
    
    def search(self,query,user=None):
        return self.get_queryset.is_public().search(query,user=user)


class Product(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20,blank=True,null=True)
    price = models.IntegerField(blank=True,default=0)
    public = models.BooleanField(default=True)

    objects = ProductManager()


    @property
    def body(self):
        return self.content
    
    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) *  0.8)
    
    @property
    def get_absulute_url(self):
        return f'api/products/{self.pk}'
    
    def get_discount(self):
        return '122'