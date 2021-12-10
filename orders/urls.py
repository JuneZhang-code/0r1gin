from django.urls import path
from django.conf.urls import include, url

from . import views
urlpatterns = [

    path('place_order',views.place_order,name='place_order'),
    #button
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),



]
