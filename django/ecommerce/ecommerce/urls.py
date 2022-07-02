
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('products/', include('product.urls')),
    path('order/', include('order.urls')),
    path('api/v1/', include('api.urls')),

]
