from django.urls import path
from django.conf.urls import include, url

from . import views
urlpatterns = [

    path('',views.shop,name='shop'),
    #button
    path('category/<slug:category_slug>/', views.shop, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),



]
