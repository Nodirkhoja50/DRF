from rest_framework.routers import DefaultRouter
from product.views import list_create_product_api_view
from product.viewset import ProductVeiwSet
router = DefaultRouter()
router.register('products',ProductVeiwSet,basename='product')
urlpatterns = router.urls