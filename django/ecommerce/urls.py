
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('products/', include('product.urls')),
    path('order/', include('order.urls'))
]
