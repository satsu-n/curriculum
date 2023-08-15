"""
URL configuration for shoppingproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import shopping.views #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shopping.views.product_list, name='product_list'),
    path('products/<int:product_id>/', shopping.views.product_detail, name='product_detail'),    #追加
    #問④-2 ここに、必要となる記述を考えて追記しましょう。
    path('products/cart/', shopping.views.product_cart, name='product_cart'),
    path('cart/<int:product_id>/add/', shopping.views.cart_add, name='cart_add'),    #追加
    #問④-4 ここに、必要となる記述を考えて記述しましょう。
    path('cart/<int:product_id>/delete/', shopping.views.cart_delete, name='cart_delete')
]
