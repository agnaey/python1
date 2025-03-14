from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('add_to_cart/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('ordered_products/', views.ordered_products, name='ordered_products'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]

