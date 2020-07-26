from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('mycart/', views.mycart_view, name='mycart'),
    path('myorders/', views.myorders_view, name='myorders'),
    path('product/<int:pk>', views.product_view, name='product'),
    path('add_to_cart/<int:pk>', views.add_to_cart_view, name='add_to_cart'),
    path('loggingout/', views.logout_view, name='logout'),
    path('search/', views.search_view, name='search'),
]