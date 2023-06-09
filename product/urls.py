from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path("",views.list_create_product_api_view,name = 'product-list'),
    path('<int:pk>',views.product_mixin_api_view),
    path('<int:pk>/update',views.product_update_api_view,name='product-update'),
    path('<int:pk>/delete',views.product_delete_api_view,name='product-delete'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path("list",views.list_product_api_view)
]